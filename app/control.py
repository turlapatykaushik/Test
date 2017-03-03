from flask import render_template
from flask import Flask, redirect, url_for, request
from app import app
from src.mysqloperations import *

@app.route('/')
def form():
	return render_template('login.html')

@app.route('/feedback')
def feedback():
	return render_template('feedback.html')

@app.route('/successUser/<name>')  
def successUser(name):
	return render_template('successUser.html',name=name)
		
@app.route('/successAd')  
def successAd():
	return render_template('successAd.html')

@app.route('/successFeedback')
def successFeedback():
	return render_template('successFeedback.html')

@app.route('/home/<name>')
def home(name):
	return render_template('home.html',name=name)

@app.route('/check',methods=['POST','GET'])
def check():
	if request.method == 'POST':
		#return "hello"
		loginDetails=request.form
		if checkLogin(loginDetails):
			return redirect(url_for('home',name=loginDetails['user_name']))
	else:
		return "send back to login"

@app.route('/addUser',methods=['POST', 'GET'])
def adduser():
	return render_template('addUser.html')

@app.route('/addAd',methods=['POST', 'GET'])
def addAd():
	return render_template('addAd.html')


@app.route('/index1',methods = ['POST', 'GET'])
def index1():
	if request.method == 'POST':
		data=request.form
		insertUser(data)
		#passLst={'type':'user'}
		#passLst['name']=user['name']
		return redirect(url_for('successUser',name=data['name']))
	else:
		return "entered else index1"
	#else:
		#user=request.args.get('name')
		#return redirect(url_for('result',name=user['name']))

@app.route('/index2',methods = ['POST', 'GET'])
def index2():
	if request.method == 'POST':
		data=request.form
		insertAd(data)
		#passLst={'type':'ad'}
		#passLst['name']=user['name']
		return redirect(url_for('successAd'))
	else:
		return "entered else index2"
	#else:
		#user=request.args.get('name')
		#return redirect(url_for('result',passLst=passLst))

@app.route('/submitFeedback',methods = ['POST', 'GET'])
def submitFeedback():
	if request.method == 'POST':
		data=request.form
		insertFeedback(data)
		#passLst={'type':'ad'}
		#passLst['name']=user['name']
		return redirect(url_for('successFeedback'))

@app.route('/users')
def users():
	users=getusers()
	return render_template('users.html',users=users)


