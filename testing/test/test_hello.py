from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Ravi") == "hello, Ravi"   


# pytest test
# The test folder should contain __init__.py