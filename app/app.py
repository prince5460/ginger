# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-17 下午3:50
@Desc :
'''
from flask import Flask


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprints(app)

    return app
