from clothing import Clothing

class Shirt(Clothing):
    def __init__(self, color, size, style, price, long_or_short):
        # calling super function to have access to all attribute and methods in parent class
        super().__init__(
            color,size,style, price,
        )
        self.long_or_short = long_or_short

    def double_price(self):
        self.price = 2*self.price
        return self.price

shirt1 = Shirt("Red",42,"old",100, "long")
print(shirt1.double_price())