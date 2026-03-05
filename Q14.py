from datetime import date

f_date = date(input("Enter 1st date(y,m,d): "))
l_date = date(input("Enter 2nd date(y,m,d): "))

delta = l_date - f_date

print(delta.days)