import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Let's ensure we are dealing with a test report
    if call.when == "call":
        outcome = call.excinfo
        try:
            # Access the test outcome (passed, failed, etc.)
            test_outcome = "failed" if outcome else "passed"
            # Access the test duration
            test_duration = call.duration
            # Access the test ID (nodeid)
            test_id = item.nodeid

            # Print Test Outcome and Duration
            print(f"Test: {test_id}")
            print(f"Test Outcome: {test_outcome}")
            print(f"Test Duration: {test_duration:.5f} seconds")
        except Exception as e:
            print("ERROR:", e) 