# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-17 下午3:50
@Desc :
'''
from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
