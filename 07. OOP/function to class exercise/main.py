class Pryamid:
    def __init__(self, height:int):
        # Validation
        assert height>=0, f"Height {height} is not greater/equal to 0"

        self.height = height
    
    def actual_pryamid(self):
        for i in range(self.height): 
            for j in range(i+1): 
                print("#", end="")
            print()
    

    def inverted_pryamid(self):
        for i in range (self.height): 
            for j in range(self.height-i-1):  
                print(" ", end="")
            for j in range(i+1):
                print("#", end="")
            print()

    def __repr__(self):
        return f"Pryamid('{self.height}')"

trail1 = Pryamid(10)
trail1.actual_pryamid()
trail1.inverted_pryamid()