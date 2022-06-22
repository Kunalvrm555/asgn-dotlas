import openpyxl
def create_excel(restaurant_name,restaurant_logo,latitude,longitude,cuisine_tags,menu_items):
    excel = openpyxl.Workbook()
    sheet = excel.active

    sheet.title = restaurant_name

    #Populate the first column of the sheet with Restaurant details

    sheet.append(["RESTAURANT DETAILS"])

    for row in zip([restaurant_name,restaurant_logo,latitude,longitude]):
        sheet.append(row)

    #insert cuisine tags of the restaurant into 5th row
    sheet.append(cuisine_tags)

    # insert a new column before the first column for row headings in RESTAURANT DETAILS section
    sheet.insert_cols(1)
    # write row headings in first column for every row
    for i, text in enumerate([ "Restaurant Name","Image URL","Latitude", "Longitude","Tags"]):
        sheet.cell(row=i+2, column=1).value = text

    sheet.append([" ","MENU ITEMS"])
    sheet.append(["Name","Description","Price (AED)","Image URL"])

    for item in menu_items: 
        sheet.append(item)


    excel.save("data/"+restaurant_name+".xlsx")

################    