import csv
from msilib.schema import Property
class Item:
    pay_rate = 0.8 # The customer need to pay after 20% discount - class attributes
    all = []

    def __init__(self, name : str, price : float, quantity =0):
        # validations for the recived arguments from the instances.
        assert price>=0, f"price {price} is not greater/equal to 0"
        assert quantity>=0, f"Quantity {quantity} is not greater/equal to 0"

        # Assign to self object or Instance
        self.__name = name # instance attributes
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    #@name.setter
    #def name(self, new_name):
     #   self.__name = new_name

        
    def calculate_total_price (self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    


    def __repr__(self):
        return f"Item('{self.name}', {self.price},{self.quantity})"
