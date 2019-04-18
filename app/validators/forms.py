# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-18 下午4:16
@Desc :
'''
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length

from app.libs.enums import ClientTypeEnum


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e

