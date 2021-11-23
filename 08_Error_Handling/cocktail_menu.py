# a function that takes in a string
# If string exists in cocktails file
# Return "Coming Right Up!"
# Otherwise return "Not on menu, sorry"

def cocktail_order(cocktail: str) -> str:
    with open("cocktails.txt") as file:
        if cocktail in file.read().split("\n"):
            return f"One {cocktail}, coming right up!"
        return "Not on the menu, sorry."


# list = """Long Island Iced Tea
# Moscow Mule
# Old Fashioned
# Mojito""".split('\n')


# for i in list:
#     print(cocktail_order(i))

# If not exists, add to menu
# Otherwise, print warning, that it already exists

def add_to_menu(cocktail: str) -> None:
    with open("cocktails.txt", "r+") as file:
        orders = file.read().split("\n")
        if cocktail in orders:
            raise Exception("Drink does not exist")
        file.write("\n" + cocktail)


new_orders = ["Coke", "Regular Ice Tea", "'Fun' On The Beach", "New Fashioned"]

for i in new_orders:
    add_to_menu(i)
