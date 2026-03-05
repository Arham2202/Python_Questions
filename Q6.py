#Q6 List and Tuple Generator
#Direct 
lst1 = [1,2,3,4,5]
tup1 = (6,7,8,9,10)

#By taking input
val = input("Enter list elements seperated by commas:")

lst2 = val.split(",")
tup2 = tuple(lst2)

print(f"List1 is {lst1} and Tuple1 is {tup1}")
print("List2 = ", lst2, "Tuple2 = ", tup2)