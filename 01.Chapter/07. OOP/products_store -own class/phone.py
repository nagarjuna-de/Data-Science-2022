from item import Item

class Phone(Item):
    
    def __init__(self, name : str, price : float, quantity =0, broken_phones=0):
        # calling super function to have access to all attribute and methods in parent class
        super().__init__(
            name, price, quantity
        )

        # validations for the recived arguments from the instances.
        assert broken_phones>=0, f"Broken phones {broken_phones} is not greater/equal to 0"

        # Assign to self object or Instance
        self.broken_phones = broken_phones