#Q18 Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1==num2==num3:
    sum = (num1+num2+num3)*3
else:
    sum = num1+num2+num3

print("The sum of the 3 numbers is: ", sum)