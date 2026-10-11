
def display_available_fuel_prices(fuel_prices):
 return fuel_prices

def dictionary_can_be_updated(fuel_old_prices, new_prices):
 fuel_old_prices.update(new_prices)
 return fuel_old_prices

def total_cost_if_liter_is_passed(new_prices, user_choice,liters):
     if user_choice not in new_prices:
       raise ValueError("Fule type is invalid")
     
     if liters <= 1 or liters > 50:
       raise ValueError("Invalid liters")
    
       unit_price = new_prices[user_choice]
     return unit_price * liters

def total_cost_if_amount_is_passed(new_prices,user_choice, amount):
     if user_choice not in new_prices:
       raise ValueError("Fule type is invalid")

     unit_price = new_prices[user_choice]

     if amount <=new_prices[user_choice]:
       raise ValueError("Invalid amount")
    
     return amount/unit_price

def record_dispenser_history(dispenser_transaction,fuel_type,liters, amount):
    if Transaction not in dispenser_history:
       dispenser_history["Transaction"] =[]
    transaction ={"fuel":fuel_type  , "price":amount, "liters":liters }
    dispenser_transaction.append["Transactions"]

    return dispenser_transaction
