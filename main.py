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
"""
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
print("Random string is string: ", isinstance(random_string, str))"""

#________________________________________________
"""
x = 10 + 5
print("X is equal", x)
number_type = x/2

print(type(number_type))

print(isinstance(number_type, int))

print(2e400) # too big
print(2e300)

num1 = 25000000
num2 = 25_000_000

print(num1, num2)

print(round(2,99))
"""

#________________________________________________
name = "Jimmy"

age = 31

age = age + 2

message = name + " is " + str(age)
message2 = f"{name} is {age}"

age = age -10
message3 = "{kat} is {dog}".format(kat=name, dog=age)

identical_text = f"""This is 
        not very
                long
        text {message2}"""

print(message3)
print(identical_text)