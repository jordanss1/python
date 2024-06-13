import sys

txt = input("Can you see this? (y/n): ")

if txt == "y" or txt == "n":
    print(F"You said: {'yes' if txt == 'y' else 'no'}")
else:
    print("Unrecognized input")
    sys.exit()

num = input("Now choose a number: ")

try:
    num = int(num)
    print(F"Your number is: {num}")
except ValueError:
    print("Please use a real number and not text")

