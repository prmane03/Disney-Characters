from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen

url = "https://api.disneyapi.dev/characters?page="
  
# store the response of URL
response = urlopen(url+"1")

# storing the JSON response 
# from url in data
alldata = json.loads(response.read())['data']

for i in range(2,150):

    # store the response of URL
    response = urlopen(url+str(i))
    
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())['data']
    # print the json response
    print(i)
    print(data_json)

    alldata = alldata + data_json

with open("DisneyCharactersJson.json","w") as outfile:
    json.dump(alldata, outfile)
