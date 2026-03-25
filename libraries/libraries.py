#########################################################
####################### Libraries #######################
#########################################################

"""
import random
coin = random.choice(["heads", "tails"])
print(coin)
"""


"""
import random as rnd
coin = rnd.choice(["heads", "tails"])
print(coin)
"""


"""
import random
number = random.randint(1, 10)
print(number)
"""



"""
import random
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards: print(card)
"""



"""
import statistics
print(statistics.mean([100, 90]))
"""



################ Command Line Arguments###############
# python .\libraries.py Ravi
"""
import sys
print("Name of the program is", sys.argv[0])
# sys.argv[0] contains the name of the program file "libraries.py"
print("hello, my name is ", sys.argv[1])
"""



"""
import sys
try:
    print("hello, my name is ", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""



"""
import sys
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments") 
else:
    print("hello, my name is", sys.argv[1])

# python libraries.py "Ravi Chandra"
# hello, my name is Ravi Chandra

# python libraries.py Ravi Chandra
# Too many arguments

# python libraries.py Ravi
# hello, my name is Ravi

# python libraries.py
# Too few arguments
"""



"""
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments") 
print("hello, my name is", sys.argv[1])

# python libraries.py Ravi Chandra
# Too many arguments
"""




"""
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
"""




################## Packages = Third party libraries ###################
##### pip can be used to install third party libraries
##### python -m pip install cowsay
"""
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])
"""
#######################################################################




############################ API Packages #############################
# python libraries.py weezer

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(response)
# print(response.text)
# print(response.json())
# print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o["results"]:
    print(result["trackName"])

#######################################################################
