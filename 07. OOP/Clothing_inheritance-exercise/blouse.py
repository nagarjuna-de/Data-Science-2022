from clothing import Clothing
class Blouse(Clothing):
    def __init__(self, color, size, style, price, country_of_origin:str):
        # calling super function to have access to all attribute and methods in parent class
        super().__init__(
            color,size,style, price,
        )
        self.country_of_origin = country_of_origin

    def triple_price(self):
        self.price = 3*self.price
        return self.price

blouse1 = Blouse("Red",42,"old",100, "India")
print(blouse1.triple_price())