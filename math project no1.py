# python code to find the entered number is divisible by 3 or not
from math import remainder

def result(user_input):
    total = 0
    while user_input != 0:
        remainder = user_input%10
        total += remainder
        user_input //= 10
    return total

user_input = int(input("enter the number = "))

if result(user_input)%3 == 0:
    print(user_input," is divisible by 3")
else:
    print(user_input," 6is not divisible by 3")
