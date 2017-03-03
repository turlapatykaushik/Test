import MySQLdb

hostname = 'us-cdbr-iron-east-04.cleardb.net'
username = 'b07dea7812b977'
password = 'ed20d511'
database = 'ad_e61f764f05bbccc'

def insertUser(data):
	db = MySQLdb.connect(host=hostname, user=username, passwd=password,db=database)
	cur = db.cursor()
	query='insert into users (name,floor,gender,twitter_id,rfidTag,ph_number,email) values ("'+data['name']+'",'+data['floor']+',"'+data['gender']+'","'+data['twitter_id']+'","'+data['rfid_tag']+'","'+data['ph_number']+'","'+data['email_id']+'")'
	cur.execute(query)
	db.commit()
	db.close()

def checkLogin(details):
	return True

def insertAd(data):
	db = MySQLdb.connect(host=hostname, user=username, passwd=password,db=database)
	cur = db.cursor()
	query='insert into advertisements (name,vendor,url,gender,personality) values ("'+data['name']+'","'+data['vendor']+'","'+data['url']+'","'+data['gender']+'","'+data['personality']+'")'
	cur.execute(query)
	db.commit()
	db.close()

def insertFeedback(data):
	db = MySQLdb.connect(host=hostname, user=username, passwd=password,db=database)
	cur = db.cursor()
	query='insert into feedback (twitter_id,rating,comments) values ("'+data['twitter_id']+'",'+data['rating']+',"'+data['comments']+'")'
	cur.execute(query)
	db.commit()
	db.close()


