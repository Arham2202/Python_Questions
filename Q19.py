#Q19 Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
txt = str(input("Enter the string- "))

def new_str(txt):
    if len(txt) >=2 and txt[:2] == "Is" :
        return txt
    else:
        return "IS " +txt
    
print(new_str(txt))
    