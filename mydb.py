import mysql.connector

# create your database connction

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'gibril',
	passwd = 'My@SirehDucsft42'
 
	)

# prepare a cursor object

cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE softcom")

print("ALL DONE!")