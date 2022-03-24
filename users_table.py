import json
from pymongo import MongoClient 
import requests as r
  
    # Making Connection
myclient = MongoClient("mongodb://localhost:27017/") 

# database 
db = myclient["TN_db"]
   
# Created or Switched to collection 
# names: GeeksForGeeks
Collection = db["users"]

# Loading or Opening the json file
with open('Users.json') as file:
    file_data = json.load(file)
      
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else inser_one is used
if isinstance(file_data, list):
    Collection.insert_many(file_data)  
else:
    Collection.insert_one(file_data)



# filter = {"name": {"$regex": r"^(?!system\.)"}}
# print(db.list_collection_names(filter=filter))
# newurl = "https://dummyapi.io/data/v1/user//post"
header = {'app-id':'6239b39aaeed12b5e056fafd'}

# store the response of URL
# data = r.get(url=gurl,headers= header).json()
newDic = {}
visited = {"60d0fe4f5311236168a109ca":False}
user_data = Collection.find({})
for user in user_data:
    for i in user['data']:
        key = i['id']
        if visited.get(key,False) == False:
            data = r.get(url=f"https://dummyapi.io/data/v1/user/{i['id']}/post",headers=header).json()
            newDic[i['id']] = data["data"]
            with open("Posts.json", "w") as outfile:
                json.dump(newDic, outfile)       
            visited[key] = True
        else:
            continue

db = myclient["TN_db"]

Collection2 = db["posts"]

# Loading or Opening the json file
with open('Posts.json') as file:
    file_data = json.load(file)
      
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else inser_one is used
if isinstance(file_data, list):
    Collection2.insert_many(file_data)  
else:
    Collection2.insert_one(file_data)

# d = dict((db, [collection for collection in myclient[db].collection_names()])
            #  for db in myclient.database_names())
# print(json.dumps(d))