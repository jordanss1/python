import hello
import sys


def func(hey):
    hello.hello()
    print(hey)

func("hey")

def greet(name, msg = "how are you!"):
     print(F"Hey {name}: {msg}")

greet("John")

greet("Dave", msg="how do you do?")

greet(msg="Ok!", name="Dave")


print(0/0)

try:
    print(0/0)
except ZeroDivisionError:
    print("ZeroDivisionError")

try:
    number = int(input("Enter a number between 1 and 10"))

    print(F"You entered the number {number}")
except ValueError:
    print("Please use only numbers")
    sys.exit()


print(number)