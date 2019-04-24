# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-24 下午3:36
@Desc :
'''
from sqlalchemy import Column, Integer, String, orm

from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    # 1、orm.reconstructor装饰器的作用：兼容SQLachemy-ORM数据库模式创建Book实例对象能去调用__init__方法
    # 2、SQLachemy-ORM创建Book【如：查询】不是通过传统的Book()创建,所以默认情况下不会调用__init__方法
    # 3、对于普通的Book()创建对象,此装饰器不影响正常初始化调用！
    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'title', 'author', 'binding',
                       'publisher',
                       'price', 'pages', 'pubdate', 'isbn',
                       'summary',
                       'image']
