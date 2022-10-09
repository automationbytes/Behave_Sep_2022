Feature: An example of scenario outline
  @Regression
  Scenario Outline: Sauce labs login
    Given the user launches the application
    Then the user verifies the logo
    When the user verifies and enters "<username>" in username field
    Then the user enters "<password>" in password field
    And the user clicks on login button

    Examples:
    |username|password|
    |standard_user|secret_sauce|
    |locked_out_user|secret_sauce|
    |problem_user   |secret_sauce|
