
class Store:
    def __init__(self,name,products=[]):
        self.name=name
        self.product=products
        #self.price=price
        #self.category=category
    def add_product(self,new_product):
        self.product.append(new_product)
        print(self.product)
        return self
    def sell_product(self,id):
        self.product.pop(id)
        return self
class Products:
    def __init__(self,name,price,type):
        self.name=name
        self.price=price
        self.category=type
    def update_price(self,percent_change,is_increased):
        if is_increased == True:
            self.price += percent_change
        else:
            self.price -= percent_change
        return self
    def print_info(self):
        print(f"Product Name:{self.name}.\nProduct Category:{self.category}.\nProduct Price:{self.price}")
    def inflation(self,percent_increase):
        new_price=self.price
        new_price += ({self.price}*{percent_increase})
        #for product in self.product:
            #new_price = self.price
            #new_price += ({self.price} * {percent_increase})
            #print old then new price
    #def set_clearance(self,category,percent_discount):
        
    #    if category == True:
    #        for self.name in self.product:
    #            if category == True:
    #                self.price -= percent_discount
    #                print(f"{self.name} has decreased to {self.price}")

store1="Walmart"
store2="TacoBell"
product1=Store("Walmart","Eggs")
product1=Store("Walmart","Yogurt")
product1=Store("Walmart","Muffins")
product1=Store("Walmart","Ethernet")

product1.add_product("Eggs")

#methods for store class:

#add_product(self, new_product) - takes a product and adds it to the store
# 
#sell_product(self, id) - remove the product from the store's list of products 
# given the id (assume id is the index of the product in the list) and print its
#  info.
# 
#inflation(self, percent_increase) - increases the price of each product by the 
# percent_increase given (use the method you wrote in the Product class!)
# 
#set_clearance(self, category, percent_discount) - updates all the products matching
#  the given category by reducing the price by the percent_discount given (use the 
# method you wrote in the Product class!)


#methods for product class:
# 
#  update_price(self, percent_change, is_increased) 
# - updates the product's price. If is_increased is True, the price should
#  increase by the percent_change provided. If False, the price should decrease
#  by the percent_change provided.
# 
# print_info(self) - print the name of the product,
#  its category, and its price.
