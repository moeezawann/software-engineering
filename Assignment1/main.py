recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        self.ingredients = ingredients

        for item, needed_amount in recipes.items(): # this for loop goes over the recipes dictionary
             if needed_amount < self.machine_resources:
                print(f("Not enough "{ingredient}" to make sandwich"))
                return False
             elif self.machine_resources < needed_amount:
                print(f("Not enough "{ingredient}" to make sandwich"))
                return False
        return True
                
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
           total_amount = 0
           dollar = int(input("How many dollars: ")) * 1
           half_dollar = int(input("How many half dollars: ")) *.5
           quarter = int(input("How many quarters: ")) *.25
           nickel = int(input("How many nickels: ")) * .05
           total_amount = dollar + half_dollar + quarter + nickel
           return total_amount




    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
            cost = self.process_coins() #reassiging cost to the amount of money given 
            for size, items in recipes.count():  # iterating over the recipes and geting the cost of each sandwich
                coins = items['cost']
                if cost >= coins:
                    return True
                else:
                    return False


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""


### Make an instance of SandwichMachine class and write the rest of the codes ###

SandwichMachine(resources)
