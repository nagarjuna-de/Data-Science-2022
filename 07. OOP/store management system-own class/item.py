import csv
class Item:
    pay_rate = 0.8 # The customer need to pay after 20% discount - class attributes
    all = []

    def __init__(self, name : str, price : float, quantity =0):
        # validations for the recived arguments from the instances.
        assert price>=0, f"price {price} is not greater/equal to 0"
        assert quantity>=0, f"Quantity {quantity} is not greater/equal to 0"

        # Assign to self object or Instance
        self.name = name # instance attributes
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

        
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
