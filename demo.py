class Product:
    def __init__(self, Product_ID, Product_NAME, Category):
        self.Product_ID = Product_ID
        self.Product_NAME = Product_NAME
        self.Category = Category
        
        self.__Sell_price = 0
        self.__Available_stock = 0

    def update_SP(self, sp):
        if sp < 0:
            print("Selling price cannot be less than 0.\n")
        else:
           
            self.__Sell_price = sp
            print(f"Selling price updated to {self.__Sell_price}\n")

    def add_stock(self, quantity):
        if quantity > 0:
            self.__Available_stock += quantity
            print(f"Stock added. New Total Stock: {self.__Available_stock}\n")
        else:
            print("Quantity must be greater than 0.\n")

    def sell(self, quantity):
        if quantity <= 0:
            print("Cannot sell zero or negative quantity.\n")
            return
        
        if self.__Available_stock >= quantity:
            self.__Available_stock -= quantity
            print(f"Sold {quantity} units of {self.Product_NAME}\n")
        else:
            print(f"Not enough stock. Have {self.__Available_stock}, need {quantity}.\n")

    def apply_discount(self, percentage):
        if 0 < percentage <= 30:
            
            discount_amount = self.__Sell_price * (percentage / 100)
            new_price = self.__Sell_price - discount_amount
            
            if new_price > 0:
                self.__Sell_price = new_price
                print(f"Discount applied. New Price: {self.__Sell_price}\n")
            else:
                print("Price would go to zero or negative, cannot apply.\n")
        else:
            print("Discount percentage must be between 1% and 30%.\n")

    def display(self):
        print(f"Product ID: {self.Product_ID}")
        print(f"Product Name: {self.Product_NAME}")
        print(f"Category: {self.Category}")
        print(f"Current Selling Price: {self.__Sell_price}")
        print(f"Available Stock: {self.__Available_stock}")
        print()
    

def get_product(number):
    print(f"Enter details of p{number}:")
    product_id = int(input("Product ID: "))
    name = input("Product name: ")
    category = input("Category: ")
    return Product(product_id, name, category)


p1 = get_product(1)
p2 = get_product(2)
p3 = get_product(3)
p4 = get_product(4) 


p1.update_SP(200)
p2.update_SP(0)
p3.update_SP(300)
p4.update_SP(500)

p1.add_stock(90)
p2.add_stock(0)
p3.add_stock(33)
p4.add_stock(50)

p1.sell(45)
p2.sell(4)
p3.sell(45)
p4.sell(5)

p1.apply_discount(15)
p1.apply_discount(50)
p1.apply_discount(-15)
p1.apply_discount(15)

p1.display()
p2.display()
p3.display()
p4.display()
