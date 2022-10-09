from behave import given, then, when
from selenium import webdriver
from PageObjects.homePage import homePage
from PageObjects.LoginPage import LoginPage

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(30)
driver.maximize_window()
hp = homePage(driver)
lp = LoginPage(driver)

@given(u'the user launches the application')
def the_user_launches_the_application(context):
    context.driver = driver
    context.driver.get("https://www.saucedemo.com/")

@then(u'the user verifies the logo')
def the_user_verifies_the_logo(context):
    context.driver = driver
    logo = context.driver.find_element(By.XPATH,"//div[@class='bot_column']")
    assert logo.is_displayed() is True

@when(u'the user verifies and enters username in username field')
def the_user_verifies_and_enters_username_in_username_field(context):
    context.driver = driver
    lp.enterUserName("standard_user")

@then(u'the user enters password in password field')
def the_user_enters_password_in_password_field(context):
    context.driver = driver
    lp.enterPassWord("secret_sauce")


@then(u'the user clicks on login button')
def theuserclicksonloginbutton(context):
    context.driver = driver
    lp.clickLogin()


@given(u'the user verifies the homepage logo')
def the_user_verifies_the_homepage_logo(context):
    context.driver =driver
    applogo = context.driver.find_element(By.XPATH,"//div[@class='app_logo']")
    assert applogo.is_displayed() is True

@then(u'the user filters low to high')
def the_user_filters_low_to_high(context):
    hp.selectFilterOption("Price (low to high)")


@when(u'the user verifies and enters "{username}" in username field')
def enter_username(context,username):
    lp.enterUserName(username)

@then(u'the user enters "{password}" in password field')
def enter_password(context,password):
    lp.enterPassWord(password)
