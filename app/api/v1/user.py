# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-17 下午4:19
@Desc :
'''
from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'Hello World!'
