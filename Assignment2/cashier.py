class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        total_amount = 0.0
        dollar = int(input("How many dollars: ")) * 1
        half_dollar = int(input("How many half dollars: ")) *.5
        quarter = int(input("How many quarters: ")) *.25
        nickel = int(input("How many nickels: ")) * .05
        total_amount = dollar + half_dollar + quarter + nickel
        return total_amount


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            remainder = float(coins - cost)
            print(f"here is ${remainder:.2f} in change ")
            return True
        else:
            print("Sorry that's not enough money. Money Refunded")
            return False
        

    
