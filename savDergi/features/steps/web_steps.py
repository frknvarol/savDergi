# features/steps/web_steps.py
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ==================== GIVEN steps ====================

@given('I am on the website')
@given('I am on the home page')
def step_visit_home(context):
    print(f"  → Navigating to {context.base_url}")
    context.driver.get(context.base_url)
    time.sleep(1)


@given('I am on the login page')
def step_visit_login(context):
    url = f"{context.base_url}/admin/"
    print(f"  → Navigating to {url}")
    context.driver.get(url)
    time.sleep(1)

# ==================== WHEN steps ====================

@when('I enter username "{username}"')
def step_enter_username(context, username):
    print(f"  → Entering username: {username}")
    username_field = context.driver.find_element(By.NAME, 'username')
    username_field.clear()
    username_field.send_keys(username)


@when('I enter password "{password}"')
def step_enter_password(context, password):
    print(f"  → Entering password: {'*' * len(password)}")
    password_field = context.driver.find_element(By.NAME, 'password')
    password_field.clear()
    password_field.send_keys(password)


@when('I click the login button')
def step_click_login(context):
    print(f"  → Clicking login button")
    login_button = context.driver.find_element(By.CSS_SELECTOR, '#login-form > div.submit-row > input[type=submit]')
    login_button.click()
    time.sleep(2)



# ==================== THEN steps ====================

@then('I should see the Site administration header')
def step_verify_dashboard(context):
    print(f"  → Verifying Site administration header")

    try:
        header = context.driver.find_element(By.CSS_SELECTOR, '#content > h1')
        assert header.is_displayed(), "Error message not visible"
        print(f"     header found: {header.text}")
    except:
        raise AssertionError("No header found on page")



@then('I should see an error message')
def step_verify_error(context):
    print(f"  → Verifying error message is displayed")
    try:
        error = context.driver.find_element(By.CLASS_NAME, 'errornote')
        assert error.is_displayed(), "Error message not visible"
        print(f"     Error found: {error.text}")
    except:
        raise AssertionError("No error message found on page")


@then('I should remain on the login page')
def step_verify_still_login(context):
    print(f"  → Verifying still on login page")
    current_url = context.driver.current_url
    print(f"     Current URL: {current_url}")
    assert 'login' in current_url.lower(), f"Expected to be on login page, but URL is {current_url}"
