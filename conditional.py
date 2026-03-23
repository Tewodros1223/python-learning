"""#grade cheker
grade = int(input("Enter your grade: "))
if grade >= 90:
    print("You got an A+")
elif grade >= 85:
    print("You got an A")    
elif grade >= 80:
    print("You got a A-")
elif grade >= 75:
    print("You got a B+!")
elif grade >= 70:
    print("You got a B")
elif grade >= 65:
    print("You got a B-")
elif grade >= 60:
    print("You got a C+")
elif grade >= 50:
    print("You got a C")
else:
    print("You failed.")

#using nested if statements find maximum of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2:
    if num1 >= num3:
        print("The maximum number is:", num1)
    else:
        print("The maximum number is:", num3)
else:
    if num2 >= num3:
        print("The maximum number is:", num2)
    else:
        print("The maximum number is:", num3)

# using match case statement to find the day of the week
day = int(input("Enter a number (1-7) to find the day of the week: "))
match day:
    case 1:        print("Monday")
    case 2:        print("Tuesday")
    case 3:        print("Wednesday")
    case 4:        print("Thursday")
    case 5:        print("Friday")
    case 6:        print("Saturday")
    case 7:        print("Sunday")
    case _:        print("Invalid input. Please enter a number between 1 and 7.")

    #using while loop with break statement to find the sum of numbers until user enters 0
total_sum = 0
while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total_sum += num
print("The total sum is:", total_sum)
"""
#using for loop with continue statement to print even numbers from 1 to 20
list_of_numbers = range(1, 21)
print("Even numbers from 1 to 20:")
for number in list_of_numbers:
    if number % 2 != 0:
        continue
    print(number)
