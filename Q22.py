#Q22 Python program to count the number 4 in a given list.
lst1 = list(map(int, input("Enter numbers separated by space: ").split()))

count = 0

for num in lst1:
    if num == 4:
        count+=1

print(f"There are {count} 4s in the given list")
