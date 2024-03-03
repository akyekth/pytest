# sample code to explain how pytest_generate_tests work

import pytest

def add(a, b):
    return a + b

# Define the data for test case generation
test_data = [
    ((1, 2), 3),   # Input: (1, 2) | Expected Output: 3
    ((0, 0), 0),   # Input: (0, 0) | Expected Output: 0
    ((-1, 1), 0),  # Input: (-1, 1) | Expected Output: 0
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



# Define the actual test function
def test_addition(test_input, expected_output):
    print("test_started")
    result = add(*test_input)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"