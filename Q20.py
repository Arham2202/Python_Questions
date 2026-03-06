#Q20 Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
text = str(input("Enter the string- "))
n = int(input("Enter how many times you need to prin the string: "))

result = ""

for i in range(n):
    result = result + text

print(result)