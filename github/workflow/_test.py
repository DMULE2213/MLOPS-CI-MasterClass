import pytest 

# function to test the square
def square(n):
    return n ** 2

# function to test cube
def cube(n):
    return n ** 3


# function to test fifth
def fifth_power(n):
    return n ** 5

# test the square fuction
def test_square(n):
    assert square(2) == 4, " Test failed: square of 2 should be 4"
    assert square(3) == 9, " Test failed: square of 3 should be 9"


# test the cube function
def test_cube(n):
    assert cube(2) == 8, " Test failed: cube of 2 should be 8"
    assert cube(3) == 27, " Test failed cube of 3 should be 27"


# test the fifth_power
def test_fifth_power(n):
    assert fifth_power(2) == 32, " Test failed: fifth power of 2 should be 32"
    assert fifth_power(3) == 243, " Test failed: Fifth power of 3 should be 243"


# test for invalid input 
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
