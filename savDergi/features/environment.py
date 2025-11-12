# features/environment.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    """Setup that runs once before all tests"""
    print("\n" + "=" * 70)
    print("Setting up test environment...")
    print("=" * 70)

    # Configuration
    context.base_url = 'http://127.0.0.1:8000'
    context.timeout = 10


def before_scenario(context, scenario):
    """Setup that runs before each scenario"""
    print(f"\n{'=' * 70}")
    print(f"Starting Scenario: {scenario.name}")
    print(f"{'=' * 70}")

    # Setup Chrome driver
    options = webdriver.ChromeOptions()
    # Comment out the headless line to watch tests live
    # options.add_argument('--headless')  # Add this back for headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--start-maximized')  # Start with maximized window

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    context.driver.implicitly_wait(context.timeout)


def after_scenario(context, scenario):
    """Cleanup that runs after each scenario"""
    if scenario.status == 'failed':
        print(f"\nScenario FAILED: {scenario.name}")
        # Take screenshot on failure
        screenshot_name = f"screenshots/{scenario.name.replace(' ', '_')}.png"
        try:
            context.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved: {screenshot_name}")
        except:
            pass
    else:
        print(f"\nScenario PASSED: {scenario.name}")

    # Close browser
    context.driver.quit()
    print(f"{'=' * 70}\n")


def after_all(context):
    """Cleanup that runs once after all tests"""
    print("\n" + "=" * 70)
    print("Test suite completed!")
    print("=" * 70)