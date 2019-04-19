# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-19 下午3:31
@Desc :
'''

from werkzeug.exceptions import HTTPException


class ClientTypeError(HTTPException):
    code = 400
    description = (
        'client is invalid'
    )
