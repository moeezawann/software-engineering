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

        for ingredient in ingredients: # this for loop goes over the recipes dictionary
             if ingredients[ingredient] > self.machine_resources[ingredient]:
                print(f"Not enough {ingredient} to make sandwich")
                return False
        return True 
                
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


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for items in order_ingredients: 
            self.machine_resources[items] -= order_ingredients[items]

        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    #had to make the report method as doing it inside a while loop would not be optimal/reusable
    def ingrident_report(self):
        for ingridient, amount in self.machine_resources.items():
            #googled/stack overflowed how to capitlize the first word 
            print(f"{ingridient.capitalize()}: {amount} slice(s)")
        
    
            

### Make an instance of SandwichMachine class and write the rest of the codes ###
make_sandwiches = SandwichMachine(resources)


while True: 
    response = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if response == 'off':
        break
    elif response in recipes:
        sandwich = recipes[response]
        needed_items = sandwich['ingredients']
        cost = sandwich['cost']
        if make_sandwiches.check_resources(needed_items):
            given_money = make_sandwiches.process_coins()
            if make_sandwiches.transaction_result(given_money, cost):
                make_sandwiches.make_sandwich(response, needed_items)
    elif response == 'report':
        make_sandwiches.ingrident_report()
    else:
        print("that is not a valid size")


     
     
    



    
  
    