import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
cashier = 0
while True:
    print(f"cashier : ${round(cashier,2)}")
    menu = input("DO you want to see the menu? 'y' or 'n'?")
    if menu == "n":
        sys.exit()
    print("Beverage\tCost")
    print("----------------------")

    # Print the items and costs from the MENU dictionary
    for key in MENU:
        cost = MENU[key]["cost"]
        print(f"{key}\t$ {cost}")
    for item in resources:
        print(item, "\t", resources[item])

    order = input("What would you like to have?")
    penny = int(input("How many penny do you have?"))
    quarter = int(input("How many quarter do you have?"))
    nickel = int(input("How many nickel do you have?"))
    dime = int(input("How many dime do you have?"))

    moneysystem = {"penny": 0.01, "quarter": 0.25, "dime": 0.1, "nickel": 0.05}

    amtpaid = (
        (penny * moneysystem["penny"])
        + (quarter * moneysystem["quarter"])
        + (nickel * moneysystem["nickel"])
        + (dime * moneysystem["dime"])
    )

    for key in MENU:
        if order == key:
            change = round(amtpaid - MENU[key]["cost"], 2)
            if change < 0:
                print("not enough money")
                sys.exit()

            for temp in resources:
                if MENU[order]["ingredients"][temp] > resources[temp]:
                    print("NOT ENOUGH RESOURCES, SORRY FOR INCONVINIENCE.")
                    sys.exit()
                resources[temp] -= MENU[order]["ingredients"][temp]
    cashier += amtpaid - change
    print(f"Enjoy your {order}")
    print(f"Here is your spare change ${change}")
