outer = ["outer1", "outer2", "outer3"]
nest = ["nest1", "nest2", "nest3"]

for x in outer:
    for y in nest:
        print(x,y)

for x in outer:
    print(x)
    for y in nest: 
        print(y)

outer = [1,2,3]
inner = ["a", "b", "c", "d", "e"]

for x in outer:
    print(x)
    for y in inner:
        print(y)