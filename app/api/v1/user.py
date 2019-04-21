# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-17 下午4:19
@Desc :
'''
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

api = Redprint('user')


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    return 'Hello World!'


@api.route('/create')
def create_user():
    pass
