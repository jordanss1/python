employees = ["Sara", "Tammy", "Debbie", "John", "Carrie"]

print(F"{employees[-1]} is a great employee!")

devices = ["IPad", "iPhone", "Android", "Charger"]

print(F"{devices[-1]} is good for {devices[0]}")

print(F"{devices[1]} is of type {type(devices[1])}")

employees[0] = "Mark"

employees = employees + ["Jim"]

print(employees)

ages = [28, 40, 33, 21, 29]

employees_and_ages = employees + ages

print(employees_and_ages)

employees.insert(1, "Alex")

print(employees)

del employees[1]

print(employees)

employees.remove("Mark")

print(employees)

for employee in employees: 
    print(employee)

if "Sara" in employees:
    print("Sara works here") 

print(len(employees))

colors = ["red", "green", "blue", "yellow", "purple"]

print(colors)

colors[3] = "brown"

print(colors)

del colors[2]

print(colors)

colors.insert(2, "gold")

print(colors)

