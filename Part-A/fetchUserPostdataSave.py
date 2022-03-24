import json
from pymongo import MongoClient 
import requests as r


# Fetching the User data from Database
  
myclient = MongoClient("mongodb://localhost:27017/") 
db = myclient["TN_db"]
Collection = db["users"]


header = {'app-id':'6239b39aaeed12b5e056fafd'}

# Fetching and creating file for post data
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

# Using Post.json to save In database
db = myclient["TN_db"]

Collection2 = db["posts"]

with open('Posts.json') as file:
    file_data = json.load(file)
      
if isinstance(file_data, list):
    Collection2.insert_many(file_data)  
else:
    Collection2.insert_one(file_data)