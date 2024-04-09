import random
from datetime import datetime, timedelta
import colorama
from colorama import Fore

w = Fore.WHITE
r = Fore.RED
b = Fore.LIGHTBLACK_EX
g = Fore.LIGHTGREEN_EX
c = Fore.CYAN
m = Fore.LIGHTMAGENTA_EX
ll = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
fr = Fore.RESET
ly = Fore.LIGHTYELLOW_EX

def generate_credit_card():
    card_number = input(f"{lr}Enter the credit card number: ")

    # Generate a random expiration date (valid for the next 10 years)
    current_year = datetime.now().year
    expiration_year = random.randint(current_year, current_year + 10)
    expiration_month = random.randint(1, 12)
    expiration_date = datetime(expiration_year, expiration_month, 1) + timedelta(days=30)
    expiration_date = expiration_date.strftime("%m/%Y")

    # Generate a random CVV (3-digit number)
    cvv = random.randint(100, 999)

    return card_number, expiration_date, cvv

# Generate the credit card details
card_number, expiration_date, cvv = generate_credit_card()

# Print the generated details
print(f"{r}Generated Credit Card Details:")
print(f"{b}Card Number:{lr}", card_number)
print(f"{b}Expiration Date:{lr}", expiration_date)
print(f"{b}CVV:{lr}", cvv)