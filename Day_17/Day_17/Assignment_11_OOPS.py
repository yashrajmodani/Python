class FoodItem:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def display_info(self):
        print(f"Name: {self.name}\nPrice: {self.price}\nCategory: {self.category}")


class Customer:
    def __init__(self,name,customer_id):
        self.name = name
        self.customer_id = customer_id
        self.order_history =[]

    def place_order(self,food_item,qty):
        self.order_history.append({"food_item":food_item,"qty":qty, "amount":food_item.price * qty})

    def view_order_history(self):
        for item in self.order_history:
            print(item)


class RegularCustomer(Customer):
    def __init__(self,name,customer_id):
        super().__init__(name,customer_id)
        self.discount = 0.05

    def place_order(self,food_item,qty):
        total = food_item.price * qty
        amt = total - total * self.discount
        self.order_history.append({"food_item": food_item, "qty": qty, "amount":amt})


class PremiumCustomer(Customer):
    def __init__(self,name,customer_id,priority_delivery):
        super().__init__(name,customer_id)
        self.discount = 0.15
        self.priority_delivery = False

    def place_order(self,food_item,qty):
        total = food_item.price * qty
        amt = total - total * self.discount
        self.order_history.append({"food_item": food_item., "qty": qty, "amount":amt})



class Restaurant:
    menu = []
    customer = []
    def add_food_item(self,food_item):
        self.menu.append(food_item)
        print(self.menu)

    def add_customer(self,customer):
        self.customer.append(customer)

    def display_menu(self):
        print(f"Menu: {self.menu}")

    def display_customer(self):
        print(f"Menu: {self.customer}")



apple = FoodItem("apple", 130, "Fruit")
banana = FoodItem("banana", 10, "Fruit")
orange = FoodItem("orange", 150, "Fruit")

mayur = RegularCustomer("Mayur",123456,)
gagan = PremiumCustomer("gagan",456789,True)



toit = Restaurant()
toit.add_food_item(apple)
toit.add_food_item(banana)
toit.add_food_item(orange)
toit.add_customer(mayur)
toit.add_customer(gagan)

mayur.place_order(apple,3)
mayur.view_order_history()
gagan.place_order(orange,5)
gagan.view_order_history()

# for i in toit.menu:
#     i.display_info()

# for i in toit.customer:
#     i.display_customer()
# toit.display_customer()

# cust = Customer("Mayur",123456)
# cust.place_order(apple,3)
# # cust.place_order('Nana',100)
# # cust.place_order('Zeher',5)
# cust.view_order_history()
