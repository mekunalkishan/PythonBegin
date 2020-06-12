ex_string = "Just do it!"
#Access the "!" from the variable by index and print() it
print (ex_string[10])

#Print the slice "do" from the variable
print(ex_string[5:7])

#Get and print the slice "it!" from the variable
print(ex_string[8:11])

#Print the slice "Just" from the variable
print(ex_string[:4])

#Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".
#Print the resulting string.
print("Don't "+ex_string[5:11])

print(type(ex_string))

print ("This is \n next line")
