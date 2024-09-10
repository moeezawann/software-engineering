# This code was created by: Moeez Awan on 9/4/24
# This code simulates a bank account with a balance, deposit, and withdraw functions
class BankAccount: 
    bankName = "Bank of America"
    # constructor
    def __init__(self,customer_name,current_balance,minimum_balance):
        self.name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, deposit) -> int:
        self.current_balance += deposit
        return self.current_balance
    
    def withdraw(self, amount) -> int:
        if(self.current_balance - amount < self.minimum_balance):
            print("You are exceeding your minimum balance withdrawl!")
        else:
            self.current_balance -= amount
            
    def printInfo(self) -> str:
           return f"{self.bankName} \nName: {self.name} \nAccount Balance: ${self.current_balance} \nMinimum Balance: ${self.minimum_balance}"

    
p1 = BankAccount("Moeez",1200,500)
p1.withdraw(900)
print(p1.printInfo())
print("")
p2 = BankAccount("Barry",3000,400)
print(p2.printInfo())
p2.deposit(2000)
print(p2.printInfo())