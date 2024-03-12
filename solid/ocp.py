"""
[Open-Closed Principle (OCP)] Download the python file from this link. 
Suppose we have a Product class that represents a generic product, and we want to calculate the total price of a list of products. 
Initially, the Product class only has a price attribute, and we can calculate the total price of products based on their prices.
Now, let's say we want to add a discount feature, where some products might have a discount applied to their prices. 
To add this feature, we would need to modify the existing Product class and the calculate_total_price function, which violates the Open/Closed Principle. 
Redesign this program to follow the Open-Closed Principle (OCP) which represents “Software entities (classes, modules, functions, etc.) 
should be open for extension, but closed for modification.”
"""

class Product:
    def __init__(self, price):
        self.price = price


class Discount:
    discount = 0.2
    @classmethod
    def get_final_price(cls,price):
        return (1-cls.discount) * price
        
class VIPDiscount(Discount):
    discount = 0.4
    @classmethod
    def get_final_price(cls, price):
        return (1-cls.discount) * price
    
def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += VIPDiscount().get_final_price(product.price)
    return total_price

# Using the calculate_total_price function with a list of products
products = [Product(100), Product(50), Product(75)]
print("Total Price:", calculate_total_price(products))
