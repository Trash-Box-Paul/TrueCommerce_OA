# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    # Test name: login
    # Step # | name | target | value
    # 1 | open | /f8a2c782-de47-4307-b690-bee136c44790/saml2?SAMLRequest=fZLNbtswEITvfQqBd0nUr2XCUuDGCGogbdVY6aGXgqZWCQGKdLmU3bx9ZSlGk6DNdbE7M9hvVle%2Fe%2BUdwaI0uiRRQIkHWphW6oeS3Dc3fkGuqg8r5L2KD2w9uEd9B78GQOetEcG68e7aaBx6sDuwRyng%2Fu62JI%2FOHZCFIT6hgz7Q4HCQDgJh%2BnASC7lA4m1GIam5m9wvN8o8SB30UliDpnNGK6nny67gsVgUsd9CuvDThC78fb6k%2Fh4gSnKRposlneWJd2OsgClwSTquEIi33ZTkZ55FNEmLWOQ8SrM2S5YpL7pM0CxfZMskH9ew5ojyCH8PEQfYanRcu5LENI58mvs0aWjBkphlNMiK%2FAfxamucEUZ9lHr%2B4GA1MxwlMs17QOYE260%2F37I4oGw%2FLyH71DS1X3%2FdNcT7fiERn0mMbDSy%2Bffvax2ejUk1o2JTYvtS4X0BfoFJqjOGkcLpdHqD7bAKX4pXl1Z8GdW2m9ooKZ68tVLmdG2Bu%2FF9zg4wkei5%2B79%2FFETTRLZ%2BN60y6LlU67a1gGNJdvXZ4dvAlewk2Lko%2F05Iwuo55OuyVn8A&RelayState=_cd462e6007f75b84ab7afb9c6926de3b | 
    self.driver.get("https://login.microsoftonline.com/f8a2c782-de47-4307-b690-bee136c44790/saml2?SAMLRequest=fZLNbtswEITvfQqBd0nUr2XCUuDGCGogbdVY6aGXgqZWCQGKdLmU3bx9ZSlGk6DNdbE7M9hvVle%2Fe%2BUdwaI0uiRRQIkHWphW6oeS3Dc3fkGuqg8r5L2KD2w9uEd9B78GQOetEcG68e7aaBx6sDuwRyng%2Fu62JI%2FOHZCFIT6hgz7Q4HCQDgJh%2BnASC7lA4m1GIam5m9wvN8o8SB30UliDpnNGK6nny67gsVgUsd9CuvDThC78fb6k%2Fh4gSnKRposlneWJd2OsgClwSTquEIi33ZTkZ55FNEmLWOQ8SrM2S5YpL7pM0CxfZMskH9ew5ojyCH8PEQfYanRcu5LENI58mvs0aWjBkphlNMiK%2FAfxamucEUZ9lHr%2B4GA1MxwlMs17QOYE260%2F37I4oGw%2FLyH71DS1X3%2FdNcT7fiERn0mMbDSy%2Bffvax2ejUk1o2JTYvtS4X0BfoFJqjOGkcLpdHqD7bAKX4pXl1Z8GdW2m9ooKZ68tVLmdG2Bu%2FF9zg4wkei5%2B79%2FFETTRLZ%2BN60y6LlU67a1gGNJdvXZ4dvAlewk2Lko%2F05Iwuo55OuyVn8A&RelayState=_cd462e6007f75b84ab7afb9c6926de3b")
    # 2 | setWindowSize | 550x691 | 
    self.driver.set_window_size(550, 691)
    # 3 | click | id=i0116 | 
    self.driver.find_element(By.ID, "i0116").click()
    # 4 | type | id=i0116 | Paul.Wu@truecommerce.com
    self.driver.find_element(By.ID, "i0116").send_keys("Paul.Wu@truecommerce.com")
    # 5 | click | id=idSIButton9 | 
    self.driver.find_element(By.ID, "idSIButton9").click()
    # 6 | mouseOver | id=idSIButton9 | 
    element = self.driver.find_element(By.ID, "idSIButton9")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 7 | type | id=i0118 | Smokingman527
    self.driver.find_element(By.ID, "i0118").send_keys("Smokingman527")
    # 8 | click | id=idSIButton9 | 
    self.driver.find_element(By.ID, "idSIButton9").click()
    # 9 | click | id=idBtn_Back | 
    self.driver.find_element(By.ID, "idBtn_Back").click()
  
