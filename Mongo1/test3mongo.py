import pymongo

client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.zpaa4mb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)



#collection is equivalent to a table in SQL dtabases
# that includes all documents.

#in terms of mongodb below dictionary is called as a
#document(an entry to the collection(table) in database below
data  = {
    "name": "kaushik",
    "surname":"samant",
    "mail":"kaushiksamant17@gmail.com",
    "subject":"DATA SCIENCE",
    "exp":10
}

#creation of database
database = client["myinformation"]

#creation of collection where we can store document
cc = database["personal_details"]

#inserting the document data  in collection "personal details"
cc.insert_one(data)
