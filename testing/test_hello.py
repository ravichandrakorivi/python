"""
from hello import hello

def test_hello():
    assert hello("Ravi") == "hello, Ravi"
    # This will not work because hello() function is not returning anything.
"""


from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Ravi") == "hello, Ravi"   