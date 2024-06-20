"""Check whether the site is available
import requests
r = requests.get('https://google.com')
print(r.status_code)"""

#___________________________________

"""amount = 20
cookie_price = 10
candy_price = 5

rest = amount - cookie_price

if rest >= candy_price:
    print("You can have a candy!")
else:
    print("No money, no honey!")"""

#___________________________________

random_number = 999
print("Random number is: ",random_number)

type_random_number = type(random_number)
print("Random number type is: ", type_random_number)

random_bool = True
print("Random number is: ", random_bool)

type_random_bool = type(random_bool)
print("Random number type is: ", type_random_bool)

random_string = "Order received. Expect results."
print("Random number is: ", random_string)

type_random_string = type(random_string)
print("Random number type is: ", type_random_string)

#check whether the variable is suggested type
print("Random string is string: ", isinstance(random_string, str))