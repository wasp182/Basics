# cartesian product of two  lists

burger = ["beef","chicken","spicy chicken"]
toppings = ["cheese","spam","eggs","beans"]

cartesian = [(bur,top) for bur in burger for top in toppings]
print(cartesian)

order_cartesian = [[(bur,top) for bur in burger] for top in toppings]
print(order_cartesian)