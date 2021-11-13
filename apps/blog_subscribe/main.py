from flask import Blueprint, request, jsonify
import json
import os
from pathlib import Path

import auth

api = Blueprint('blog_subscribe', __name__)


DB = Path(__file__).parent.joinpath('mail_list.json')

def load():
    with open(DB) as f:
        return json.load(f)

def save(data):
    with open(DB, 'w') as f:
        json.dump(list(set(data)), f)

def add(email):
    data = load()
    data.append(email)
    save(data)
    return 'Successfully added!'

def remove(email):
    data = load()
    try:
        data.remove(email)
        save(data)
        return 'Successfully removed!'
    except ValueError:
        return 'Email was not subscribed!'


if not DB.exists():
    save([])


@api.route('/blog_subscribe', methods=['POST', 'DELETE', 'GET'])
def rest_api():
    mail = request.args.get('mail', None)
    token = request.args.get('token', None)

    if request.method in ['POST', 'DELETE']:
        if mail is None:
            return jsonify({'result': 'Error, expected mail as kwargs.'})

        if request.method == 'POST':
            result = add(mail)
        else:
            if token is None:
                result = 'You must have authentication token!'
            else:
                if auth.authenticate(token):
                    result = remove(mail)
                else:
                    result = 'Invalid authentication'

        return jsonify({'result': result})

    elif request.method == 'GET':
        if token is None:
            result = 'You must have authentication token!'
        else:
            if auth.authenticate(token):
                result = load()
            else:
                result = 'Invalid authentication'

        return jsonify({'result': result})