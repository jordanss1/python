import hello

def func(hey):
    hello.hello()
    print(hey)

func("hey")

def greet(name, msg = "how are you!"):
     print(F"Hey {name}: {msg}")

greet("John")

greet("Dave", msg="how do you do?")

greet(msg="Ok!", name="Dave")