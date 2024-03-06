# sample code to explain how pytest_generate_tests work

import pytest

def add(a, b):
    return a + b

# Define the data for test case generation
test_data = [
    pytest.param((1, 2), 3,marks=pytest.mark.xray('EVA-11469')),   # Input: (1, 2) | Expected Output: 3
    pytest.param((0, 0), 0,marks=pytest.mark.xray('EVA-11470')),   # Input: (0, 0) | Expected Output: 0
    pytest.param((-1, 1), 0,marks=pytest.mark.xray('EVA-11471'))  # Input: (-1, 1) | Expected Output: 0
]

# Define the pytest_generate_tests hook to generate test cases
def pytest_generate_tests(metafunc):
    
    if 'test_input' in metafunc.fixturenames:        
        # Generate test cases based on the test_data list
        # method takes the names of the fixtures to be filled 
          # (test_input and expected_output in this case) 
          # and the data to fill them with (test_data).
        # this function is nothing but parametrize(varibles, inputdata)
        
        metafunc.parametrize('test_input,expected_output', test_data)
        # for test_args in test_data:
        #     metafunc.parametrize('marker', [pytest.mark.xray(test_args[2])])



# Define the actual test function
def test_addition(test_input, expected_output):
    print("test_started")    
    result = add(*test_input)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"