from flask import Flask, make_response, jsonify
from werkzeug.routing import Rule
import os

from .controller.elasticsearch import elasticsearch_router

APP_ROOT = os.getenv('APP_ROOT')

if not APP_ROOT is None:
    class Custom_Rule(Rule):
        def __init__(self, string, *args, **kwargs):
            prefix = APP_ROOT
            super(Custom_Rule, self).__init__(prefix + string, *args, **kwargs)

def create_app():
    app = Flask(__name__)
    if not APP_ROOT is None:
        app.url_rule_class = Custom_Rule
    app.register_blueprint(elasticsearch_router, url_prefix='/')
    return app

app = create_app()