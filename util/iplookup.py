import requests
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

def phone_locator(phone_number, api_key):
    url = f"https://api.apilayer.com/number_verification/validate?number={phone_number}"
    headers = {
        "apikey": api_key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def print_phone_details(phone_details):
    print(f"{lr}Phone Details: {b}")
    print(f"{lr}Number: {b}{phone_details['number']}")
    print(f"{lr}Country: {b}{phone_details['country_name']} ({phone_details['country_code']})")
    print(f"{lr}Carrier: {b}{phone_details['carrier']}")
    print(f"{lr}Line Type: {b}{phone_details['line_type']}")
    print(f"{lr}Location: {b}{phone_details['location']}")
    print(f"{lr}Valid: {b}{phone_details['valid']}")

api_key = "22WfDqB635jMOWkxdeC1r2BXew1tXHLU"

phone_number = input(Fore.RED + f"IP : {b}")

phone_details = phone_locator(phone_number, api_key)
print_phone_details(phone_details)