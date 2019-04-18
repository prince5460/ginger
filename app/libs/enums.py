# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-18 下午4:14
@Desc :
'''
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 小程序
    USER_MINA = 200
    # 微信
    USER_WX = 201
