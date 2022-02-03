class Clothing:
    # constructor and Attributes.
    def __init__(self, color : str, size, style: str, price):
        assert price>=0, f"price {price} is not greater/equal to 0"
        # attributes.
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    # changing price and assigning it to self.price
    def change_price(self, price):
        self.price = price
        return self.price

    # calculating discount price after removing discount.
    def calculate_discount(self, discount):
        discount_price = self.price*(1-discount)
        return discount_price

    # shipping_price
    def calculate_shipping(self, weight, rate):
        shipping_price = weight*rate
        return shipping_price
    

    def __repr__(self):
        return f"Clothing('{self.color}', {self.size},{self.style},{self.price})"



clothing1 = Clothing('Red',50, 'New', 50)
print(clothing1.color)

 
