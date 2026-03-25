########################### Variables & Functions ###########################

# Side effects
print("Hello")                  
print("hello, world")           

# Ask user for their name
name = input("What's your name? ")


# Say hello to the user

# print() function can take muliple arguments. 
# Python will automatically insert spaces in between the arguments.
print("Hello,", name)           # Hello, Ravi

# Single argument to print() function
print("Hello, " + name)         # Hello, Ravi

# Format string as a parameter to print() function
print(f"Hello, {name}")         # Hello, Ravi

print("Hello,", end=" ")
print(name)                      # Hello, Ravi

print("Hello,", name, sep="???")    # Hello,???Ravi

# The default values of 'sep' and 'end' parameters are " " and "\n" respectively


# Funcftions on string data types or string methods
name = input("What's your name? ")
name = name.strip()
# name = name.capitalize()
name = name.title()
print(f"Hello, {name}")

name = input("What's your name? ")
name = name.strip().title()