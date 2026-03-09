"""
from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()
"""



"""
from calculator import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__":
    main()
"""



"""
from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")

    try:
        assert square(3) == 9
    except:
        print("3 squared was not 9")

    try:
        assert square(-5) == 25
    except:
        print("-5 squared was not 25")
    
    try:
        assert square(0) == 0
    except:
        print("0 squared was not 0")

if __name__ == "__main__":
    main()
"""




#####################################################################################
########### Unit Tests : Testing indicidual units/functions of our program ##########
#####################################################################################
#python -m pip install pytest

"""
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

#pytest .\test_calculator.py
"""



from calculator import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9    

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")