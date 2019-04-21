# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-19 下午3:31
@Desc :
'''

from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = 'sorry,we make a mistake.'
    error_code = 999


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 400
    msg = 'the resource are not found... '
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed '
    error_code = 1005
