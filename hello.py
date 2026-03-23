y = 24
x = f"my name is tewodros Kassa 'i am {y} years old'"

print(x.isalpha())
#boolean 
z = 30
if z > y:
    print ("30 is greater than 24 ")
else:
    print ("display the error") 
#operators
#arthimethic operator
x, y = 2, 3  
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)
print(x % y)
print(x // y)
 #assignment operator
print(x:=5)
 #list display by loop 
thislist = ["orage", "banana", "apple", "mango"]
m = thislist[0]
n = thislist[1]
o = thislist[2]
p = thislist[3]
print(m, n, o, p)
for i in range(len(thislist)):
    print(thislist[i])
#dictionary
fruits = {"banana" : "yellow",
        "apple" : "red",
        "mango" : "orange"}
print (fruits.values())  
print(fruits["banana"])  