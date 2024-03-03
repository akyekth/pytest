# Test Math Functions  
import pytest

@pytest.mark.parametrize( "a, b, expected",  
    [  
        (1, 2, 3),  
        (5, -1, 4),  
    ],)  
def test_addition(a, b, expected):  
    assert a+b == expected 