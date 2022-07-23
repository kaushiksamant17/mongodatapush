#import package
import pymongo
#pip install pymongo
#you need to install pip install pymongo[srv]

#make sure when you create password and user create a simple
#password or user id and dont include @ in password

# establish a connection
client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.zpaa4mb.mongodb.net/?retryWrites=true&w=majority")

# test the connection by calling it
db = client.test

#print the connection status and if it's print then it is proper
print(db)

k = {
    "name":"kaushik",
    "age":"samant",
    "age":33
}

db1 = client['mongotest']
col1 = db1['test2']
col1.insert_one(k)

kk ={
    "name":"sachin",
    "surname":"samant",
    "age":30
}

db2 = client["mongotest"]
col2 = db2['test2']
col2.insert_one(kk)





'''# since it is on cloud here we can connect sudhanshu sir's mongo db server
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)'''