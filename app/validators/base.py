# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-19 下午5:04
@Desc :
'''
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self, data):
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)