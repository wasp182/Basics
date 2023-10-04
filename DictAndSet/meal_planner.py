from contents import recipes,pantry

# present menu with keys in recipe , and values = ingredient
# transfer keys of recipe as values to menu_dict , key(menu)= index+1
# values(menu) = key(recipe)
# ask for selection from menu and go back to recipe to get ingredient

menu_dict = {}
for index,meal in enumerate(recipes):
    menu_dict[str(index+1)]=meal


def add_item_shopping(shopping_list: dict, food_item: str, quantity_buy: str):
    if food_item not in shopping_list:
        shopping_list[food_item] = quantity_buy
    else:
        shopping_list[food_item] += quantity_buy
    return shopping_list

shopping_list = {}
while True:
    print("____________________________")
    print("Please select meal from menu")
    for key, value in menu_dict.items():
        print(f"{key}: {value}")

    choice= input(": ")
    if choice =="0":
        break
    elif choice in menu_dict:
        selected_meal = menu_dict.get(choice)
        print(f"you have selected {selected_meal}")
        print("check ingredient")
        ingredients = recipes.get(selected_meal)
        print(ingredients)
        for food_item,quantity in ingredients.items():
            available_foodQuant = pantry.get(food_item,0)
            if available_foodQuant >= quantity:
                print(f'{food_item} required {quantity}. Available is {available_foodQuant}'
                      f' \n Good to go')
            else:
                quantity_buy= quantity-available_foodQuant
                print(f'ran out of {food_item}. Buy {quantity_buy}')
                add_item_shopping(shopping_list,food_item,quantity_buy)
                # shopping_list[food_item] = quantity_buy
        print(shopping_list)



