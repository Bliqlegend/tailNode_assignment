import requests as r
import json
from pymongo import MongoClient 

gurl = "https://dummyapi.io/data/v1/user/"
header = {'app-id':'6239b39aaeed12b5e056fafd'}

data = r.get(url=gurl,headers= header).json()

# print the json response
json_object = json.dumps(data,indent = 4) 
print(json_object)

# save in file
with open("Users.json", "w") as outfile:
    json.dump(data, outfile)

# Use the Users.json file to Save in database
myclient = MongoClient("mongodb://localhost:27017/") 

db = myclient["TN_db"]
   
Collection = db["users"]

with open('Users.json') as file:
    file_data = json.load(file)
      
if isinstance(file_data, list):
    Collection.insert_many(file_data)  
else:
    Collection.insert_one(file_data)
