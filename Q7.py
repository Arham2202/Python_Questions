#Q7 File extension extractor
filename = input("Input the Filename: ")

f_extn = filename.split(".")

print("The extension of the file is : ", repr(f_extn[-1]))