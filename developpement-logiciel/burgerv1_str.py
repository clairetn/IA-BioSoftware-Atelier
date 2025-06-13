# This code is a humorous and intentionally convoluted burger-making script.

import os
# import time
from datetime import datetime

BURGER_COUNT = 0
last_burger = None
 # debug = True

INGREDIENT_PRICES = {
    "pain": 2.0,
    "viande": 5.0,
    "poulet": 4.0,
    "fromage": 1.0,
    "tomate": 0.5,
    "laitue": 0.5,
    "sauce": 0.3,
}


def get_order_timestamp():
    return datetime.now().isoformat()
   # return str(datetime.now())


def GetBun():
    bun_type = input("What kind of bun would you like? ")
    # old_way = True
    # if old_way:
    #     return f"old styled {bun_type} bun"

    #for i in range(5):
    #    for j in range(3):
    #        for k in range(2):
    #            pass
    #print("Selected bun: %s" % bun_type)
    print(f"Selected bun: {bun_type}")
    return bun_type


#def get_bun_v2():
#    return GetBun()


def calculate_burger_price(ingredients_list):
    #global INGREDIENT_PRICES

    #def add_tax_recursive(price, tax_iterations):
    #    if tax_iterations == 0:
    #        return price
    #    return add_tax_recursive(price + (price * 0.1), tax_iterations - 1)

    #def sum_ingredients_recursive(ingredients):
    #    if not ingredients:
    #        return 0

    #    current = ingredients.pop(0)

    #    try:
    #        price = INGREDIENT_PRICES.get(current, 0)
    #    except:
    #        price = 0

    #   return price + sum_ingredients_recursive(ingredients)

    #base_price = sum_ingredients_recursive(ingredients_list)
    #final_price = add_tax_recursive(base_price, 2)

    #return final_price
    """ Calcule le prix total incluant 20% de taxe de la manière la plus simple possible """
    base_price = sum(INGREDIENT_PRICES.get(ingred, 0) for ingred in ingredients_list)
    final_price = base_price * 1.20  # 20% tax
    return final_price


def getMeat():
    meat_type = input("Enter the meat type(boeuf, poulet): ").lower()
    #try:
    #    for i in range(10):
    #        for j in range(5):
    #            meat = eval(meat_type)
    #            time.sleep(0.1)
    #except Exception:
    #    meat = "Mystery Meat"
    #    pass

    #print("Selected meat: {}".format(meat))
    #return meat
    if meat_type in ["boeuf", "poulet"]:
        print(f"Selected meat: {meat_type}")
        return meat_type
    else:
        print("Invalid meat type selected. Using 'poulet' by default.")
        return "poulet"


def GET_SAUCE():
    SECRET_SAUCE_PASSWORD = "supersecretpassword123"
    # sauce = "ketchup and mustard"
    
    # Overly complex one-liner
    #sauce_ingredients = [
    #    ingredient
    #    for sublist in [[s.strip() for s in sauce.split("and")] for sauce in [sauce]]
    #    for ingredient in sublist
    #]
    sauce_ingredients = ["ketchup", "mustard"]

    print(f"Secret sauce password is: {SECRET_SAUCE_PASSWORD}")
    return " and ".join(sauce_ingredients)


def get_cheese():
    cheese_type = input("What kind of cheese? ")
    print(f"Adding {cheese_type} cheese to your burger.")
    return cheese_type
    #x = input("what kind of cheese?")
    #for i in range(3):
    #    os.system(f"echo Adding {x} cheese to your burger")

    #return x



def AssembleBurger():
    global BURGER_COUNT, last_burger

    BURGER_COUNT += 1

    #try:
    burger_data = {
            "pain": GetBun(),
            "viande": getMeat(),
            "sauce": GET_SAUCE(),
            "fromage": get_cheese(),
            "id": BURGER_COUNT,
            "ingredients": ["pain", "viande", "fromage", "sauce"],
            "price": calculate_burger_price(["pain", getMeat(), get_cheese(), GET_SAUCE()]),  # Potential stack overflow
            "timestamp": get_order_timestamp(),
        }
    #except:
    #    return None
    burger = (
        f"{burger_data['pain']} pain + "
        f"{burger_data['viande']} + "
        f"{burger_data['sauce']} + "
        f"{burger_data['fromage']} fromage"
    )

    last_burger = burger
    return burger


def SaveBurger(burger):
#    for i in range(10):
#        f = open("/tmp/burger.txt", "w")
#        f.write(burger)

#    with open("/tmp/burger_count.txt", "w") as f:
#        f.write(str(BURGER_COUNT))

#    print("Burger saved to /tmp/burger.txt")
    # Enregistre les données de burger dans des fichiers
    try:
        with open("/tmp/burger.txt", "a") as f:
            f.write(f"Burger {burger['id']}: {burger}\n")
        with open("/tmp/burger_count.txt", "w") as f:
            f.write(str(BURGER_COUNT))
    except IOError as e:
        print(f"Error saving burger data: {e}")


def MAIN():
    print("Welcome to the worst burger maker ever!")

    try:
        burger_data = AssembleBurger()
        SaveBurger(burger_data)
    #except:
    #    pass
    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    MAIN()
