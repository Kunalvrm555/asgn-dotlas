import openpyxl
def create_excel(restaurant_name,restaurant_logo,latitude,longitude,cuisine_tags,menu_items):
    # create new excel workbook and select a sheet
    excel = openpyxl.Workbook()
    sheet = excel.active

    # Populate the first column of the sheet with Restaurant details

    # RESTAURANT DETAILS section
    sheet.append(["RESTAURANT DETAILS"])

    # insert restaurant details in first column
    for row in zip([restaurant_name,restaurant_logo,latitude,longitude]):
        sheet.append(row)

    # insert cuisine tags of the restaurant into 5th row
    sheet.append(cuisine_tags)

    # insert a new column before the first column for row headings in RESTAURANT DETAILS section
    sheet.insert_cols(1)
~
    # insert row headings in first column for every row
    for i, text in enumerate([ "Restaurant Name","Image URL","Latitude", "Longitude","Tags"]):
        sheet.cell(row=i+2, column=1).value = text

    # MENU ITEMS section
    sheet.append([" ","MENU ITEMS"])

    # insert column headings for items in menu
    sheet.append(["Name","Description","Price (AED)","Image URL"])

    # for each item  in the list menu_items 
    # insert items into subsequent rows
    for item in menu_items: 
        sheet.append(item)

    # save the sheet titled as the restaurant name in 'data' folder
    excel.save("data/"+restaurant_name+".xlsx")

################    