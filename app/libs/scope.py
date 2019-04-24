# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-23 下午4:03
@Desc :
'''


class AdminScope:
    allow_api = ['v1.super_get_user']


class UserScope:
    allow_api = ['v1.get_user']


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False
