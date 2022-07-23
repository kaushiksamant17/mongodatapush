#1
import mysql.connector as conn

#2
mydb = conn.connect(host = "localhost",user = "root",passwd = "root")

#3
cursor2 = mydb.cursor()

#thisis just query assigned to variable s
#s = "insert into kaush.test values(24121,'testing',98000)"

#4
#cursor2.execute(s)

''' normally in sql while working in pythong we need 4 statemsntes
first import , secon create a connection , third create a pointer
using cursor function that helps to route from one database to other
and last would be using the object of cursor  executing the query
'''

#Ideally in this cases we normally where we insert we have to commit
#not applicable while creating the dtabase or table
mydb.commit()

#again firing a query and getting the output
cursor2.execute("select * from kaush.test where salary < 50000")
for i in cursor2.fetchall():
    print(i)

print("aise hi")
cursor2.execute("select * from kaush.test where salary = 88000")
for j in cursor2.fetchall():
    print(j)

print("\n"
      "timepass")
cursor2.execute("select * from kaush.test where salary > 90000")
for k in cursor2.fetchall():
    print(k)