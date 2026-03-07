"""
def main():
    student = get_student()
    # Tuple is immutable
    print(f"{student[0]} from {student[1]}")
    # name, house = get_student()
    # print(f"{name} from {house}")

    return

def get_student():
    name = input("Name: ")
    house = input("House: ")

    # Return a tuple
    # A tuple is immutable
    return (name, house)
    #return name, house

if __name__ == "__main__":
    main()
    # When we run the file directly, __name__ will be __main__ and hence the main() function will get executed.

    # When another file imports this file, __name__ will be student. Hence, main() will NOT run automatically.
    # This lets you reuse the functions without executing the program.
"""


"""
def main():
    student = get_student()
    # Lists and dictionaries are mutable
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student["name"]} from {student["house"]}")
    return

# {"name": name, "house": house} is a dictionary
# {name, house} is a set

def get_student():
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
"""


"""
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    return

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
"""


"""
# Classes have attributes and methods.
# An instance of a class is an object.
class Student:
    # __init__() method will be called whenever Student() is instanciated
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    # __str__() method will be called when print(Student object) is called
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "🪄"

def main():
    student = get_student()

    # student.house = "Number Four, Privet Drive"
    # Attributes of student object can be modified easily by the user even by mistake.

    print(student)
    print(f"Expecto Patronum: {student.charm()}")
    return

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    # student = Student(name, house)
    # return student
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
"""


"""
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        # Above commands call their respective Setter methods
        # self._name & self._house are actually the attributes
        # self.name & self.house are properties or methods

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()

    # student.house = "Number Four, Privet Drive"
    # It will raise value error

    # student._house = "Number Four, Privet Drive"
    # It will not raise any error as it will not call setter method but will directly assign new value to the underlying object attribute 

    print(student)
    return

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

# int, list, dict, str etc are all classes

# type(50)
# <class 'int'>

# type(int())
# <class 'int'>

# type([])
# <class 'list'>

# type(list())
# <class 'list'>

# type({})
# <class 'dict'>

# type(dict())
# <class 'dict'>
"""




################## Instance/Object Methods vs Class Methods #############
# Instance Methods
"""
import random
class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

hat = Hat()

hat.sort("Harry")
"""

"""
# Class Methods
import random
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")
"""

"""
class Student:

    # Object / Instance method
    def __init__(self, name, house):
        self.name = name
        self.house = house
        # Above commands call their respective Setter methods
        # self._name & self._house are actually the attributes
        # self.name & self.house are properties or methods

    # Object / Instance method
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Class method
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    # Class method Student.get()
    student = Student.get()
    print(student)
    return

if __name__ == "__main__":
    main()
"""
########################################################################






############################### Inheritance #############################
"""
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
    
    ...

class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.subject = subject
    ...    
"""

"""
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...
        
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
"""
#########################################################################






########################## Operator Overloading ###########################
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    # operator overloading
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 25)
print(weasley)

# galleons = potter.galleons + weasley.galleons
# sickles = potter.sickles + weasley.sickles
# knuts = potter.knuts + weasley.knuts
# total = Vault(galleons, sickles, knuts)
# print(total)

total = potter + weasley
print(total)
###########################################################################









########################### functions vs methods ##########################
#import pandas

# type(pandas.read_csv)
# <class 'function'>

# type(df.head)
# <class 'method'>
# It's an instance method but not a class method.

# A function is defined independently, not tied to any specific object.
# read_csv() is a standalone function in the pandas module.

# A method is a function that belongs to a class or object.
# head() belongs to the DataFrame object
#########################################################################

