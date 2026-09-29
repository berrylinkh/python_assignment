class Account:
    def __init__(self, name: str) -> None:
        self.name = name.lower()
        self.balance = 0
        
        
    def deposit(self,amount):
        if amount < 0: 
            raise ValueError ("deposit cannot be negative")
        self.balance += amount
        
    def withdraw (self,amount):
        if amount > self.balance or amount < 0: 
            raise ValueError ("withdraw is greater than deposit")
        self.balance -= amount
        
        
        
        
#acc = Account ("Eniife")       
#acc2 = Account ("Winifred") 
