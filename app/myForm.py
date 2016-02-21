
# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,FloatField
from wtforms.validators import Required

class NameForm(Form):
	name=StringField('',validators=[Required()])
	submit=SubmitField(u'搜索客户')

class ProdForm(Form):
	namep=StringField(u'产品名称:')
	type=StringField(u'产品类型:')
	unitprice=FloatField(u'单价')
	submit=SubmitField(u'提交')

class customer(Form):
	pass


