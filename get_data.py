import requests,json
from bs4 import BeautifulSoup
def get_data(url):

    # Get the HTML from the url    
    r = requests.get(url)

    # Parse the HTML
    soup = BeautifulSoup(r.text,"html.parser")

    # print(soup.prettify())

    # HTML tree traversal

    # load script type='application/ld+json' which contains restaurant details into variable restaurant
    # json used to decode javascript objects
    restaurant = json.loads(soup.find('script', type='application/ld+json').text)

    # store the required values into variables with suitable names
    restaurant_logo = restaurant["image"]
    restaurant_name = restaurant["name"]
    latitude = float(restaurant["geo"]['latitude'])
    longitude = float(restaurant["geo"]['longitude'])
    cuisine_tags = restaurant["servesCuisine"].split(',')

    # print(restaurant_name)
    # print(restaurant_logo)
    # print(latitude)
    # print(longitude)
    # print(cuisine_tags)

    # load script type='application/ld+json' which contains menu details with additional page details into variable data
    data = json.loads(soup.find('script', type="application/json" ).text)

    # Only menu items are needed from the page
    menu = data["props"]["pageProps"]["initialMenuState"]["menuData"]["items"]

    #create an empty list in which each menu item will be stored as a list as well
    menu_items = list()

    # iterate through each menu item 
    # create a list of the required values for each menu item
    # append the list into the list menu_items

    for item in menu:
        menu_items.append([item["name"],item["description"],float(item["price"]),item["image"]])

    # print(menu_items)

    return ([restaurant_name,restaurant_logo,latitude,longitude,cuisine_tags,menu_items])