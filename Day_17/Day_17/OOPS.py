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

    def place_order(self,food_item,quantity):
        total_price = food_item.price * quantity
        order_details = {
            "food_item":food_item.name,
            'quantity':quantity,
            'total_price':total_price
        }
        self.order_history.append(order_details)
        print(f"{self.name} ordered {quantity} {food_item.name}(s) for ${total_price}")


    def view_order_history(self):
        if not self.order_history:
            print(f"{self.name} has no orders")
        else:
            print(f"{self.name}'s order history:")
            for order in self.order_history:
                print(f"{order['food_item']} x {order['quantity']} = ${order['total_price']}")


class RegularCustomer(Customer):
    def __init__(self,name,customer_id):
        super().__init__(name,customer_id)
        self.discount = 0.05

    def place_order(self,food_item,quantity):
        total_price = food_item.price * quantity
        discount = total_price * (1-self.discount)
        order_details = {
            "food_item":food_item.name,
            'quantity':quantity,
            'total_price':discount
        }
        self.order_history.append(order_details)
        print(f"{self.name} ordered {quantity} {food_item.name}(s) for ${discount} ")

class PremiumCustomer(Customer):
    def __init__(self,name,customer_id):
        super().__init__(name,customer_id)
        self.discount = 0.15
        self.priority_delivery = True

    def place_order(self,food_item,quantity):
        total_price = food_item.price * quantity
        discount = total_price * (1-self.discount)
        order_details = {
            "food_item":food_item.name,
            'quantity':quantity,
            'total_price':discount,
            'priority_delivery':self.priority_delivery
        }
        self.order_history.append(order_details)
        print(f"{self.name} ordered {quantity} {food_item.name}(s) for ${discount} ")



class Restaurant:
    def __init__(self):
        self.menu = []
        self.customers = []

    def add_food_item(self,food_item):
        self.menu.append(food_item)

    def add_customer(self,customer):
        self.customers.append(customer)

    def display_menu(self):
        if not self.menu:
            print("No items in the menu")
        else:
            print("Menu:")
            for item in self.menu:
                item.display_info()

    def display_customer(self):
        if not self.customers:
            print("No customers")
        else:
            print("Register Customers:")
            for customer in self.customers:
                print(f"{customer.name} - {customer.customer_id}")

pizza = FoodItem("Pizza",150,"Fast Food")
burger = FoodItem("Burger",120,"Fast Food")
ice_cream = FoodItem("Ice Cream",80,"Dessert")

mayur = RegularCustomer("Mayur","C0001")
gagan = PremiumCustomer("Gagan","C0002")

restaurant = Restaurant()
restaurant.add_food_item(pizza)
restaurant.add_food_item(burger)
restaurant.add_food_item(ice_cream)

restaurant.add_customer(mayur)
restaurant.add_customer(gagan)

restaurant.display_menu()
restaurant.display_customer()

mayur.place_order(pizza,2)
mayur.place_order(ice_cream,1)

gagan.place_order(burger,3)
gagan.place_order(ice_cream,1)

gagan.view_order_history()
mayur.view_order_history()