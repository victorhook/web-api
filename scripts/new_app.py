import os
from pathlib import Path


DEFAULT_CONTENT = \
"""\
from flask import Blueprint

api = Blueprint('{}', __name__)

#@api.route('/')
#def index():
#    return 'Hello'

"""

if __name__ == '__main__':
    APP_DIR = Path(__file__).parent.parent.joinpath('apps')
    app_name = None

    while app_name is None:
        app_name = input('> App name: ')
        if app_name in os.listdir(APP_DIR):
            print('That app already exists')
            app_name = None

    print(f'Creating app "{app_name}"')
    app_dir = APP_DIR.joinpath(app_name)
    os.mkdir(app_dir)

    main = app_dir.joinpath('main.py')
    with open(main, 'w') as f:
        f.write(DEFAULT_CONTENT.format(app_name))
