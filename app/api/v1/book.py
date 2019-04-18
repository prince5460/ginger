# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-17 下午4:19
@Desc :
'''
from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('', methods=['GET'])
def get_book():
    return 'get book'


@api.route('', methods=['POST'])
def create_book():
    return 'create book'
