import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    while True: 
        response = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()

        if response == 'off':
            print("Thanks for using!")
            break
        elif response in recipes:
            sandwich = recipes[response]
            needed_items = sandwich['ingredients']
            cost = sandwich['cost']
            if sandwich_maker_instance.check_resources(needed_items):
                given_money = cashier_instance.process_coins()
                if cashier_instance.transaction_result(given_money, cost):
                    sandwich_maker_instance.make_sandwich(response, needed_items)
        elif response == 'report':
            sandwich_maker_instance.ingrident_report()
        else:
            print("that is not a valid size")


if __name__=="__main__":
    main()
