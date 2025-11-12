Feature: User Login
  As a user
  I want to login to the application
  So that I can access my account

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "testuser"
    And I enter password "testuser123456?"
    And I click the login button
    Then I should see the Site administration header

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter username "wronguser"
    And I enter password "wrongpass"
    And I click the login button
    Then I should see an error message
    And I should remain on the login page
