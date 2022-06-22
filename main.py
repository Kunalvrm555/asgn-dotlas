import json
from create_excel import *
from get_data import *

# Opening JSON file
f = open('data/urls.json')
  
# returns JSON object as a dictionary
urls = json.load(f)
  
# Closing file
f.close()

# Iterating through the json list
for i, url in enumerate(urls):
    try:
        print("Currently processing URL at index",i+1)
        data = get_data(url)
        create_excel(data[0],data[1],data[2],data[3],data[4],data[5])
        print("Successfully generated sheet for "+ data[0] +" in folder 'data'")

    except:
        print("An error occurred with URL at index",i+1)

######################

