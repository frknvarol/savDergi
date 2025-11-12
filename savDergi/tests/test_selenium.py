# tests/test_selenium.py
from django.test import TestCase  # Changed from StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib.auth.models import User


class SeleniumTestCase(TestCase):
    """Base class for Selenium tests with Django"""

    # Your actual localhost URL
    live_server_url = ' http://127.0.0.1:8000'  # Change port if needed

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Set up Chrome driver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode (no GUI)
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        cls.driver.implicitly_wait(10)  # Wait up to 10 seconds for elements

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()


class HomePageTest(SeleniumTestCase):
    """Test the home page functionality"""

    def test_home_page_loads(self):
        """Test that home page loads successfully"""
        self.driver.get(f'{self.live_server_url}/')

        # Check page title
        self.assertIn('Home', self.driver.title)

        # Check for specific element
        heading = self.driver.find_element(By.TAG_NAME, 'h1')
        self.assertEqual(heading.text, 'Welcome')

    def test_navigation_links(self):
        """Test that navigation links work"""
        self.driver.get(f'{self.live_server_url}/')

        # Find and click a link
        about_link = self.driver.find_element(By.LINK_TEXT, 'About')
        about_link.click()

        # Verify we're on the about page
        self.assertIn('about', self.driver.current_url)


class LoginTest(SeleniumTestCase):
    """Test login functionality"""

    def setUp(self):
        # Create a test user
        self.username = 'testuser'
        self.password = 'testpass123'
        User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_user_login(self):
        """Test user can login successfully"""
        self.driver.get(f'{self.live_server_url}/login/')

        # Find form elements
        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

        # Fill in the form
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        # Submit the form
        submit_button.click()

        # Wait for redirect and check we're logged in
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'user-profile'))
        )

        # Verify login success
        self.assertIn('dashboard', self.driver.current_url)

    def test_invalid_login(self):
        """Test login fails with invalid credentials"""
        self.driver.get(f'{self.live_server_url}/login/')

        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

        # Use invalid credentials
        username_input.send_keys('wronguser')
        password_input.send_keys('wrongpass')
        submit_button.click()

        # Check for error message
        error_msg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'error-message'))
        )
        self.assertIn('Invalid', error_msg.text)


class FormTest(SeleniumTestCase):
    """Test form submission"""

    def test_contact_form_submission(self):
        """Test submitting a contact form"""
        self.driver.get(f'{self.live_server_url}/contact/')

        # Fill out the form
        name_input = self.driver.find_element(By.ID, 'id_name')
        email_input = self.driver.find_element(By.ID, 'id_email')
        message_input = self.driver.find_element(By.ID, 'id_message')

        name_input.send_keys('John Doe')
        email_input.send_keys('john@example.com')
        message_input.send_keys('This is a test message')

        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()

        # Wait for success message
        success_msg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'success-message'))
        )
        self.assertIn('Thank you', success_msg.text)


class JavaScriptInteractionTest(SeleniumTestCase):
    """Test JavaScript interactions"""

    def test_modal_interaction(self):
        """Test opening and closing a modal"""
        self.driver.get(f'{self.live_server_url}/')

        # Click button to open modal
        open_modal_btn = self.driver.find_element(By.ID, 'open-modal')
        open_modal_btn.click()

        # Wait for modal to be visible
        modal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'modal'))
        )
        self.assertTrue(modal.is_displayed())

        # Close modal
        close_btn = self.driver.find_element(By.CLASS_NAME, 'close-modal')
        close_btn.click()

        # Wait for modal to be hidden
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.ID, 'modal'))
        )