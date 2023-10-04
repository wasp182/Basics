from data import people , plants_list,basic_plants_list,plants_dict

# attempt to send email if available in list else we can edit receipts
# all based code fails if list given as imput is empty

# people=[]

if bool(people) and all([person[1] for person in people]):
    print("sending mail")
else:
    print("edit the recipients")


if any([plant.plant_type =="Grass" for plant in plants_list]):
    print("at least one grass plant in selection")
else: print("no grass here")


if any([plant_details.plant_type== "Grass" for plant_details in plants_dict.values()]):
    print("at least one grass in plants dictionary")
else:
    print("no grass here")