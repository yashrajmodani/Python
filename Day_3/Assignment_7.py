# inventory={}
# value_dict={}
# while 1:
#     item = input("Enter a item:")
#     quantity = int(input("Enter the quantity:"))
#     price = int(input("Enter the price:"))
#
#     inventory[item:value_dict]=

inventory = {}
num=int(input("Enter no. of items to add:"))
total_value = 0
for i in range(num):

    item_name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))

    if item_name not in inventory:
        inventory[item_name] = {"quantity": quantity, "price": price}
    else:
        inventory[item_name]["quantity"] += quantity
        inventory[item_name]["price"] = price

    print(f"Item '{item_name}' added to the inventory!")

    for a in inventory:
        total_value = quantity * price

print(inventory)
print(total_value)


inventory.clear()
print(inventory)

