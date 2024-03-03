import pytest


@pytest.hookimpl()
def pytest_sessionstart(session):
    print("Hello from `pytest_sessionstart` hook!")


@pytest.hookimpl()
def pytest_sessionfinish(session, exitstatus):
    print("Hello from `pytest_sessionfinish` hook!")
    print(f"Exit status: {exitstatus}")

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
        
# # Plugin 1
# @pytest.hookimpl(tryfirst=True)
# def pytest_collection_modifyitems(items):
#     print(f"Test Outcome: pytest_collection_modifyitems")

# Plugin 2
@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(items):
    print(f"Test Outcome: pytest_collection_modifyitems")