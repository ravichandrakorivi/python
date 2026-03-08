################################################################################## Exceptions ######################
##########################################################

# print("hello, world)
# SyntaxError: unterminated string literal (detected at line 1)


"""
x = int(input("What's x? "))
print(f"x is {x}")

What's x? apple
Traceback (most recent call last):
  File "exceptions.py", line 7, in <module>
    x = int(input("What's x? "))
ValueError: invalid literal for int() with base 10: 'apple'
"""



"""
try:
    x = int(input("What's x? "))
##except:
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
"""



"""
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
"""



"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

if __name__ == "__main__":
    main()
"""



"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

if __name__ == "__main__":
    main()
"""



"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

if __name__ == "__main__":
    main()
"""



"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
"""




def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

if __name__ == "__main__":
    main()