import MySQLdb

hostname = 'us-cdbr-iron-east-04.cleardb.net'
username = 'b07dea7812b977'
password = 'ed20d511'
database = 'ad_e61f764f05bbccc'

db = MySQLdb.connect(host=hostname, user=username, passwd=password,db=database	)
db.close()
