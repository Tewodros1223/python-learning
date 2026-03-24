"""day = 4
match day:
    case 1: print("monday")
    case 2: print("thusday")
    case 3: print("wednsday")
    case 4: print("thursday")
    case 5: print("friday")
    case 6: print("saturday")
    case 7: print("sunday")
    case _: print("invalid")
x = range(3, 10, 2)
print(x)
print(list(x))
print(9 in x)
print(len(x))
for i in range(10):
    print(i)

# array
car = ["d4d", "toyota", "landcruser"]
cars = [1, 2, 3, 4]
car.append("moterbke")
car.pop(1)
car[2] ="tomato"

for x in car+cars:
    print(x)
"""
# module
import datetime
import math
x = datetime.datetime.now()
print(x)
# built in math
x, y = 16, 4
power = pow(x, y)
absolute = abs(-7287)
squar = math.sqrt(x)
floor = math.ceil(4.75)
maxi = max(10,23,67)
mini = min(90, -23, 57)
print(power)
print(absolute)
print(squar)
print(floor)
print(maxi)
print(mini)
# none values assign to a variable
x = None
print(x)