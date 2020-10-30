#shopping cart eg

menu= {"burger": 100,
       "fries": 40,
       "pizza": 70}

print("menu: \n {}".format(menu))

menu["fries"] = 60
menu["shake"] = 100
print(menu)

item_cart = []
choice = "yes"
total = 0
while choice == "yes":
    print()
    item =input(" what would u like to add?")
    item_cart.append(menu[item])
    total += menu[item]

    choice = input("would u like to add another item? yes/no")
print(item_cart)
print("amount to pay: {}".format(total))

# mini project
