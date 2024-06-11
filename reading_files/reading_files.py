a = open("text.txt")
print(a.read())

a.close()

a = open("text.txt")
print("new", a.readline())

a.close()

a = open("text.txt")
print(a.read(7))

a.close()

with open("text.txt") as myfile:
    contents = myfile.read()
    print(contents)

with open("text.txt", "a") as myfile:
    myfile.write("\nNew line")

print(open("text.txt").read())

with open("text.txt", "w") as myfile:
    myfile.write("Overwritten!")

with open("text.txt") as myfile:
    print(myfile.read())

with open("new.txt", "x") as myfile:
    open("new.txt", "a").write("Hello, new file!")
    print(open("new.txt").read())

with open("reading_files/new2.txt", "w") as myfile:
    a = 1
    while a < 4:
        if a == 1:
            open("reading_files/new2.txt", "a").write("Hi!")
        else: 
            open("reading_files/new2.txt", "a").write("\nHi!")
        a += 1
    print(open("reading_files/new2.txt").read())





