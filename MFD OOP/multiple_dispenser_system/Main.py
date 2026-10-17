from zoneinfo import available_timezones

from multiple_dispenser_system.Dispenser import Dispenser
from multiple_dispenser_system.FuelAttendant import FuelAttendant

dispenser = Dispenser({})
attendant = FuelAttendant("Aderonke  Adeniyi", dispenser, [])

attendant.add_new_fuel("petrol", 1350, 500)
attendant.add_new_fuel("diesel", 2100, 500)
attendant.add_new_fuel("gas", 2000,500)
attendant.add_new_fuel("kerosine", 1500, 500)


main_menu ="""
    ========Welcome to Kanipe Filling Station========

        press 1 => Display available fuel
        press 2 => Choose fuel type
        press 3 => Record Transaction
        press 4 => Exit
        """

while True:
        user_selection = int(input(main_menu))

        match user_selection:
            case 1:
                available = attendant.get_available_fuel()
                print("Available fuel:",)
                for name,fuel in available.items():
                    print (f"{name}: {fuel.fuel_name}, price: {fuel.price_per_liter}, quantity: {fuel.quantity}")

            case 2:
                fuel_type = input("Choose fuel type: ").lower()
                items_available = attendant.get_available_fuel()
                if fuel_type not in items_available:
                    print("Invalid fuel type")
                    continue

                fuel = items_available[fuel_type]
                user_option = input("Are you buying in liters or amount: ").lower()

                if user_option == "liters":
                    liters = float(input("Enter number of liters: "))
                    if liters <=0:
                        print("Liters cannot be less than or equal to zero")
                    elif liters > fuel.quantity:
                        print("Liters cannot be greater than fuel quantity")
                    else:
                        transaction = attendant.dispense_fuel_by_liters(fuel_type, liters)
                        print("Transaction:", transaction)

                if user_option == "amount":
                    amount = float(input("Enter price: "))
                    if amount < fuel.price_per_liter:
                        print("Amount cannot be less than or equal to zero")
                    elif amount / fuel.price_per_liter > fuel.quantity:
                        print("Amount cannot be greater than fuel quantity")
                    else:
                        transaction = attendant.dispense_fuel_by_amount(fuel_type, amount)
                        print("Transaction:", transaction)

            case 3:
                transactions = attendant.show_all_transactions()
                if transaction == 0:
                    print("No transaction yet")
                else:
                    for transaction in transactions:
                        print(transaction)

            case 4:
                print("Thank you for visiting Kanipe Filling Station.")
                break

            case _:
                print("Invalid input")