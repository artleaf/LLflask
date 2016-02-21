# -*- coding: utf-8 -*-
from app import app
from flask import render_template,session,redirect,url_for,flash,request,escape
from flask.ext.bootstrap import Bootstrap
bootstrap=Bootstrap(app)
#import myForm
from myForm import NameForm,ProdForm

@app.route('/',methods=['GET','POST'])
def index():
	name=None
	form=NameForm()
	if form.validate_on_submit():
		session['name']=form.name.data
		#return request.form['form.name.data']
		return redirect(url_for('search'))
	return render_template('index.html',form=form,name=session.get('name'))
#	return 'hello world, hello flask'

@app.route('/prodadd',methods=['GET','POST'])
def prodadd():
	namep=None
	type=None
	unitprice=None
	formp=ProdForm()
	if formp.validate_on_submit():
		session[namep]=formp.namep.data
		session[type]=formp.type.data
		session[unitprice]=formp.unitprice.data
		return redirect(url_for('prodadd'))
	return render_template('prodadd.html',form=formp,namep=session.get('namep'),type=session.get('type'),unitprice=session.get('unitprice'))

@app.route('/customer',methods=['GET','POST'])
def customer():
	return render_template('customer.html')

@app.route('/search')
def search():
	name=escape(session.get('name'))
	return render_template('search.html',name=name)


