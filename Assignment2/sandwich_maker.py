
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients: # this for loop goes over the recipes dictionary
             if ingredients[ingredient] > self.machine_resources[ingredient]:
                print(f"Not enough {ingredient} to make sandwich")
                return False
        return True 

    def make_sandwich(self, sandwich_size, order_ingredients):
        for items in order_ingredients: 
                self.machine_resources[items] -= order_ingredients[items]

        print(f"{sandwich_size} sandwich is ready. Bon appetit!")
    
    def ingrident_report(self):
        for ingridient, amount in self.machine_resources.items():
            #googled/stack overflowed how to capitlize the first word 
            print(f"{ingridient.capitalize()}: {amount} slice(s)")