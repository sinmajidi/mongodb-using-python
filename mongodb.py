import pymongo

#first you should install mongodb on your computer and run it on a optional port
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test_database"] #this is the database name
students_table = mydb["students"] #this a a table named students

print(myclient.list_database_names()) # this command show all databased

#also we can see the items of databases list using below command:
for database in myclient.list_database_names():
    print(database)
print(mydb.list_collection_names()) # it will show all tables


#insert
# i insert the student dictionary to student_table
student = { "name": "sina", "email": "sin.majidi@gmail.com" }
x = students_table.insert_one(student)
print(x.inserted_id)

#find
#we can access to studets_table using following commands:
for x in students_table.find():
    print(x) #or print(x['name'])

#find using query:
myquery = { "name": "sina" }
mydoc = students_table.find(myquery)
for x in mydoc:
  print(x)

# delete a query
myquery = { "name": "sina" }
students_table.delete_one(myquery)

#update a query
myquery = { "name": "sina" }
newvalues = { "$set": { "name": "ali" }}
students_table.update_one(myquery, newvalues)