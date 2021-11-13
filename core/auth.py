import secrets
import binascii
from pathlib import Path

from db import DB


db = DB(Path(__file__).parent.joinpath('tokens.json'))


def authenticate(token):
    return token in db.load()

def gen_token():
    token = binascii.b2a_hex(secrets.token_bytes(64)).decode('utf-8')
    data = db.load()
    data.append(token)
    db.save(data)
    print(token)
