a, b = 5, 10
(c,d) = (10, 15)

e = f = g = 3

print(a, b)
print(e,f,g)

numbers = {"First Num": '1', "Second Num": '2'}

for key, val in numbers.items():
    print(F'Key "{key}" has a value of "{val}"')

h,i,j = 10,20,30

k,l,m,n = 33, "car", 2.158, "hey"

print(k,l,m,n)

people = {"Dave": "41", "Bob": "22", "Mark": "38"}

for key, val in people.items():
    print(F"{key} is {val}")