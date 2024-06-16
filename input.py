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

salary = 44000
txt = "You make {} dollars a year".format(salary)
print(txt)

txt = "John does {} {}".format("software", "development")
print(txt)

txt = "John has {1} {2} and loves {0}".format("bicycles", 5, "cars")
print(txt)

txt = "John likes {hobby3}, {0}, and {1}".format("running", "gaming", hobby3="cars")
print(txt)

print(str(sys.argv))
