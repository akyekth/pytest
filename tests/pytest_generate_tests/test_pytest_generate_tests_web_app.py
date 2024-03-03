import pytest
from web_app import WebApp

# Define user roles and expected permissions
user_roles = [
    ('admin', True, True),
    ('editor', True, True),
    ('viewer', False, True),
]

# Define the pytest_generate_tests hook to generate test cases
def pytest_generate_tests(metafunc):
    if 'user_role' in metafunc.fixturenames:
        # Generate test cases based on the user_roles list
        metafunc.parametrize('user_role', user_roles)

# Test function that uses the dynamically generated test cases
def test_web_app_permissions(user_role):
    user_role, can_edit, can_view = user_role  # Unpack the fixture value

    app = WebApp(user_role)
    
    assert app.can_edit_content() == can_edit, f"Unexpected edit permission for {user_role}"
    assert app.can_view_content() == can_view, f"Unexpected view permission for {user_role}"