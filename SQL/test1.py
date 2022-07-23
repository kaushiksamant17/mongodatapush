# import the package mysql and module connector
#pip install mysql-connector-python
import mysql.connector as conn

# trying to establish a connection
mydb = conn.connect(host = "localhost",user = "root",passwd = "root")
print(mydb)

#post connection, using cursor function to connect to the database
#as it acts as a pointer
cursor1 = mydb.cursor()

#now connection is done we just now to execute the query in below
#command
#cursor1.execute("show databases")

#lets create a database
cursor1.execute("create database kaush")

#create the table
cursor1.execute("create table kaush.test(empid int(10),dptname varchar(20) ,salary int)")

#this is used to fetch all the database
#print(cursor1.fetchall())
