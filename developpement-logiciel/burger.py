import os
from datetime import datetime

# Constantes globales
BURGER_COUNT = 0
last_burger = None
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


def calculate_burger_price(ingredients_list):
    base_price = sum(INGREDIENT_PRICES.get(ingred, 0) for ingred in ingredients_list)
    final_price = base_price * 1.20  # 20% tax
    return final_price


def GetBun():
    bun_type = input("What kind of bun would you like? ")
    print(f"Selected bun: {bun_type}")
    return bun_type


def getMeat():
    meat_type = input("Enter the meat type (boeuf, poulet): ").lower()
    if meat_type in ["boeuf", "poulet"]:
        print(f"Selected meat: {meat_type}")
        return meat_type
    else:
        print("Invalid meat type selected. Using 'poulet' by default.")
        return "poulet"


def GET_SAUCE():
    SECRET_SAUCE_PASSWORD = "supersecretpassword123"
    sauce_ingredients = ["ketchup", "mustard"]
    print(f"Secret sauce password is: {SECRET_SAUCE_PASSWORD}")
    return " and ".join(sauce_ingredients)


def get_cheese():
    cheese_type = input("What kind of cheese? ")
    print(f"Adding {cheese_type} cheese to your burger.")
    return "fromage"  # Utiliser "fromage" pour pricing dans INGREDIENT_PRICES


def AssembleBurger():
    global BURGER_COUNT, last_burger
    BURGER_COUNT += 1
    burger_data = {
        "pain": GetBun(),
        "viande": getMeat(),
        "sauce": GET_SAUCE(),
        "fromage": get_cheese(),
        "id": BURGER_COUNT,
        "ingredients": ["pain", "viande", "fromage", "sauce"],
        "price": calculate_burger_price(["pain", getMeat(), get_cheese(), GET_SAUCE()]),
        "timestamp": get_order_timestamp(),
    }

    burger = (
        f"{burger_data['pain']} pain + "
        f"{burger_data['viande']} + "
        f"{burger_data['sauce']} + "
        f"{burger_data['fromage']}"
    )

    last_burger = burger
    return burger_data  # Retourne le dictionary au lieu de la chaîne


def SaveBurger(burger_data):
    try:
        with open("/tmp/burger.txt", "a") as f:
            f.write(f"Burger {burger_data['id']}: {burger_data['pain']} + {burger_data['viande']} + {burger_data['sauce']} + {burger_data['fromage']}\n")
        with open("/tmp/burger_count.txt", "w") as f:
            f.write(str(burger_data['id']))
    except IOError as e:
        print(f"Error saving burger data: {e}")


def MAIN():
    print("Welcome to the improved burger maker!")
    try:
        burger_data = AssembleBurger()
        SaveBurger(burger_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    MAIN()
