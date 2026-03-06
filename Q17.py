#Q17 Python program to test whether a number is within 100 of 1000 or 2000.
num = int(input("Enter the number: "))

def diff_1000(num):
    if ((abs(1000-num)<=100) or (abs(2000-num)<=100)):
        return "The number is within 100s"
    else:
        return "The number is not within 100s"

print(diff_1000(num))

           