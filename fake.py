# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-23 上午9:20
@Desc :
'''

from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'admin'
        user.password = '123456'
        user.email = '999@qq.com'
        user.auth = 2
        db.session.add(user)
