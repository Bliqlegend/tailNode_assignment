import requests as r
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
gurl = "https://dummyapi.io/data/v1/user/"
header = {'app-id':'6239b39aaeed12b5e056fafd'}

# store the response of URL
data = r.get(url=gurl,headers= header).json()
# storing the JSON response 
# from url in data

# print the json response
json_object = json.dumps(data,indent = 4) 
print(json_object)

# save in file
with open("Users.json", "w") as outfile:
    json.dump(data, outfile)