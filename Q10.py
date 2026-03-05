#Q10 Python program that accepts an integer (n) and computes the value of n+nn+nnn.
num = int(input("Enter an Integer:"))

n1 = int("%s%s" %(num,num))
n2 = int("%s%s%s" %(num, num, num))

print(num + n1 + n2)