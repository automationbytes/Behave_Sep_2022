Feature: SauceLabs Ecommerce Site
  @Sanity @Regression
  Scenario: Sauce Lab Login
    Given the user launches the application
    Then the user verifies the logo
    When the user verifies and enters username in username field
    Then the user enters password in password field
    And the user clicks on login button

  Scenario: Filter by Low to High
    Given the user verifies the homepage logo
    Then the user filters low to high