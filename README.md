# pytest
diffrent examples of pytest
planning is write
-   fixtures
-   diffrent type of hooks
- how to run the project
cmd> tox 
    -   tox.ini has 3 environments
    -   when we run tox it will create 3 environments
    -   now select path for python interpreter:  tox-run/scripts/python.exe
    -   when we run tox it will install dependecies mentioned in (requirements.in) file
- files explanation
   - pyproject.toml and setup.py file both create project as python package.
- pytest hooks:
  -  https://pytest-with-eric.com/hooks/pytest-hooks/
  -  pytests hooks 6types
     by using these hooks can change the flow of a framework
     - Bootstrapping hooks
     - Intialize hooks
     - collection hooks
     - tetsrunning hooks
     - reporting hooks
     - debugging hooks
- order of execution when we have hooks
   - tryfirst-> 1. hook: pytest_session starts
                2. pytest: test session start
                3. hook: pytest_collection_modifyitems
                4. pytest: collecting all tests
                5. pytest: Execute test1
                6. hook: pytest_runtest_makereport
                7. pytest: execute tes2
                8. hook: pytest_runtest_makereport
                9. hook: pytest_session_hook_finish
                10. pytest:finished running tests

-  pytest_generate_tests
   - Can I Use Pytest Hooks to Dynamically Generate Tests based on Certain Conditions?
   - ans: yes
   - TDD- test driven development
   - method: pytest_generate_tests'
   - guide: https://pytest-with-eric.com/introduction/pytest-generate-tests/
   -  parameterized testing can help produce tests with varying input data, it has its limitations. For example, it can be challenging to generate test cases with complex logic or extensive data manipulation.
   - where pytest-generate-tests step in, offering a versatile and comprehensive approach beyond what parameterized testing can achieve.

- Pytest Hypothesis Library
    - property based tetsing:Pytest Hypothesis Library - unittests+hypothesis
      - link:https://pytest-with-eric.com/pytest-advanced/hypothesis-testing-python/
      -  testcases generated based on contariants or conditions
## JIRA-INTEGRATION
1. Create testcases in jira manually. or create testcases in xcel sheet and upload to jira.
2. Collect the test case key
3. and open your pytest cases and specify by using @pytest.mark.xray('JIRA-1')
4. create 3 environmental vraibles
    - XRAY_API_BASE_URL - 'https://<....>.com/'
    - XRAY_API_USER  - jira username
    - XRAY_API_PASSWORD - jira_password
5. run test by using below command
```
commnad upload tests specific test execution: pytest --jira-xray --execution <te-key-XXXX>
commnad create new test execution: tests specific test execution: pytest --jira-xray
```
6. after running above command can see below lineas output
---------- Uploaded results to JIRA XRAY. Test Execution Id: XXX-XXXX ----------        
