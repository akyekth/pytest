import pathlib 
import os

import pytest
import json
import requests

from datetime import datetime,timezone, timedelta
from pluggy import HookspecMarker

hookspec = HookspecMarker("pytest")
def pytest_addoption(parser):
    question_path = pathlib.Path(__file__).parent / "test_example" / "test_suite.json"
    parser.addoption("--test_suite", default=question_path, help="path to test suite")
    parser.addoption("--test-exe", default="<te-key>", help="path to test suite")


def generate_date():
    # print(file_path)
    current_dt = datetime.now()
    # Define the timezone offset
    offset = timedelta(hours=1)  # +01:00
    # Apply the timezone offset to the current datetime object
    current_dt_with_offset = current_dt.replace(tzinfo=timezone(offset))
    # Format the datetime object to the desired format
    formatted_date = current_dt_with_offset.strftime("%Y-%m-%dT%H:%M:%S%z")    
    return formatted_date

def pytest_sessionstart(session):

    output_file_name = "test_results.json"
    if os.path.exists(output_file_name):
        os.remove(output_file_name)
    
    if os.path.exists(output_file_name):
        print("File exists")
    else:
        print("File does not exist")
    formatted_date = generate_date()
    print(formatted_date)
    file_info_object= {
                        "testExecutionKey": "test_key",
                        "info": {
                        "summary": "Execution of automated tests for release v1.1",
                        "user": "<user>",
                        "startDate": formatted_date,
                        "finishDate": "2014-08-30T11:53:00+01:00",
                        "testEnvironments": [
                        "SIT"
                        ]
                        },
                        "tests": []
                      }

    
    with open(output_file_name, "w") as f:
        json.dump(file_info_object,f, indent=2)
        f.write("\n")  # Initialize with empty list
    print("finish creating a file")
    



@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Let's ensure we are dealing with a test report
    if call.when == "call":
        outcome = call.excinfo
        test_key = item.callspec.params["test_key"]
        print("iam in hook: test key is ",test_key)        
        try:
            # Access the test outcome (passed, failed, etc.)
            test_outcome = "FAIL" if outcome else "PASS"
            # Access the test duration
            if test_outcome == "FAIL":
                if call.excinfo is not None:
                    # Test failed, handle the exception
                    exception_type = call.excinfo.type
                    exception_value = call.excinfo.value
                    exception_traceback = call.excinfo.traceback
                comment = str(exception_type) + "\n" + str(exception_value)

            else:
                comment = "Successful execution"
            test_duration = call.duration
            # Access the test ID (nodeid)
            test_id = item.nodeid
            print("test_id")
            test_deatils= {
                            "status": test_outcome,
                            "testKey": test_key,
                            "comment": comment,
                            "executedBy": "aruna"                 
                          }
            # Print Test Outcome and Duration
            print(f"Test: {test_id}")
            print(f"Test Outcome: {test_outcome}")
            print(f"Test Duration: {test_duration:.5f} seconds")
            with open("test_results.json", "r") as f:
                json_data= json.load(f)
            json_data["tests"].append(test_deatils)
            input_file_name = "test_results.json"
            # Save the updated JSON back to the file
            with open(input_file_name, "w") as file:
                json.dump(json_data, file, indent=4)
        except Exception as e:
            print("ERROR:", e) 


def pytest_sessionfinish(session, exitstatus):
    config= session.config
    print("Test session is ending")
    HEADERS_JIRA={"Content-Type": "application/json"}
    JIRA_BASEURL = "<url>"
    ending_time= generate_date()
    print(ending_time)
    output_file= "test_results.json"
    with open(output_file, "r") as f:
        data = json.load(f)
    data["info"]["finishDate"] = ending_time
    # data["testExecutionKey"] = test_exe
    print(data)
    jira_url= JIRA_BASEURL+ 'rest/raven/2.0/import/execution'
    jira_username = 'xxxx'
    jira_pwd = 'yyyyyy'
    res = requests.post(jira_url,
                        auth=(jira_username, jira_pwd),
                        headers=HEADERS_JIRA,
                        json = data)
    print(res.json())
    print(res.status_code)
    print(res.text)



