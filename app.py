from posixpath import join
from flask import Flask, jsonify
from flask_cors import CORS

import os
import importlib
from pathlib import Path
import sys

BAS_DIR        = Path(__file__).parent
APP_DIR        = BAS_DIR.joinpath('apps')
CORE_DIR       = BAS_DIR.joinpath('core')
APP_NAME       = 'main'
BLUEPRINT_NAME = 'api'

app = Flask(__name__)
CORS(app)

def get_app_dirs():
    app_paths = [os.path.join(APP_DIR, app) for app in os.listdir(APP_DIR)]
    app_paths = list(filter(lambda p: os.path.isdir(p), app_paths))
    return app_paths

def import_app(app_dir):
    try:
        # Build module path & name for import
        app_module = os.path.join(app_dir, APP_NAME)
        app_module = '.'.join(app_module.split('/')[-3:])
        # Import module
        app_module = importlib.import_module(app_module)
        # Import api from module
        app_ = getattr(app_module, BLUEPRINT_NAME)
        return app_
    except ModuleNotFoundError:
        print(f'App {app_dir} does not have a "main.py" with "api" obj inside. Skipping...')
        return None

def register_apps():
    app_dirs = get_app_dirs()
    registered_apps = []
    for dir in app_dirs:
        app_ = import_app(dir)
        if app_ is not None:
            app.register_blueprint(app_)
            registered_apps.append(app)

    print(f'Registered total of {len(registered_apps)} apps')


# Add core lib to path
sys.path.append(str(CORE_DIR))

# Register all found apps.
register_apps()
server_info = [{'url': rule.rule, 'method': rule.endpoint} for rule in app.url_map._rules]


@app.route('/info')
def url_map():
    return jsonify(server_info)
