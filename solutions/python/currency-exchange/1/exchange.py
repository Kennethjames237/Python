"""Functions for calculating steps in exchanging currency."""

def exchange_money(budget, exchange_rate):
    return float(budget/exchange_rate)

def get_change(budget, exchanging_value):
    return float(budget-exchanging_value)
    
def get_value_of_bills(denomination, number_of_bills):
    return int(denomination*number_of_bills)

def get_number_of_bills(amount, denomination):
    return int(amount/denomination)
    
def get_leftover_of_bills(amount, denomination):
    number_of_bills = get_number_of_bills(amount, denomination)
    value_of_bills = get_value_of_bills(denomination,number_of_bills)
    return float(amount - value_of_bills)

def exchangeable_value(budget, exchange_rate, spread, denomination):
    new_exchange_rate = (exchange_rate * (spread / 100)) + exchange_rate
    total_currency = exchange_money(budget, new_exchange_rate)
    max_exchangeable = int( total_currency // denomination * denomination)
    return max_exchangeable

