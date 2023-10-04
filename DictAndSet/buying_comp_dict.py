available_parts = {"1":"computer",
                   "2":"monitor",
                   "3":"keyboard",
                   "4":"mouse",
                   "5":"hdmi cable",
                   "6":"dvd drive",
                   }

current_choice=" "
chosen_dict={}
##Coding challenge solution:
# while current_choice!="0":
#     if current_choice in available_parts:
#         chosen_part= available_parts[current_choice]
#         if chosen_part in chosen_list:
#             print(f'removing {chosen_part}')
#             chosen_list.remove(chosen_part)
#         else:
#         print(f"adding {chosen_part}")
#         chosen_list.append(chosen_part)
#     else:
#         print('add parts from list')
#         for index,parts in available_parts.items():
#             print("{0} : {1}".format(index,parts))
#     current_choice=(input(':> '))

while current_choice!="0":
    if current_choice in available_parts:
        chosen_part= available_parts[current_choice]
        if current_choice in chosen_dict:
            print(f'removing {chosen_part}')
            chosen_dict.pop(current_choice)
        else:
            print(f"adding {chosen_part}")
            chosen_dict[current_choice]=chosen_part
        print(f'your dictionary has : {chosen_dict}')
    else:
        print('add parts from list')
        for index,parts in available_parts.items():
            print("{0} : {1}".format(index,parts))
    current_choice=(input(':> '))
