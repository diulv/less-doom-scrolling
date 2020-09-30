from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

usernameField = find_element_by_name("session[username_or_email]")
passwordField = find_element_by_name("session[password]")

browser = webdriver.Firefox()
username = username
password = password

browser = webdriver.Firefox()
broswer.get("https://www.twitter.com/login")
time.sleep(10)

username_field = browser.find_element_by_name("session[username_or_email]")
password_field = browser.find_element_by_name("session[password]")
        
username_field.send_keys(username)
password_field.send_keys(password)
username_field.send_keys(Keys.RETURN)
