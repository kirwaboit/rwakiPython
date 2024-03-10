import os

from flask import Flask


def create_app(test_config = None):
    app = Flask(_name_)
    app.config.from_mapping(
        SECRET_KEY  = os.environ.get('SECRET_KEY', default = 'dev')
    )
