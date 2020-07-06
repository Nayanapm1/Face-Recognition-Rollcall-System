import pymysql

db=pymysql.connect("localhost","root","INFO5717!","rollcall")

cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchone()

print("Database version:%s"%data)
db.close()