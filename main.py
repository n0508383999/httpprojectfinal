from flask import Flask, request, json, Response
import logging as log
import instraction
import pymongo
# import gridfs
#db = MongoClient().gridfs_example
#fs = gridfs.GridFS(db)
client = pymongo.MongoClient('localhost', 5000)
mydb=client["movie_poster"]
mycol=mydb["posters"]
print (mydb.list_collection_names())
dataone={"name":"ezoo","sur":"attrash"}
datalist=[{"name":"hiba","sur":"najjar"},{"name":"moanes","sur":"najjar"}]
x=mycol.insert_many(datalist)
print (x.inserted_ids)
for x in mycol.find({"name" :"hiba"},{"_id":0}) :
    print (x.values())
instraction.write(dataone)
