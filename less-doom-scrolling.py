from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = username
password = password

browser = webdriver.Firefox()

browser.get("https://www.twitter.com/login")
time.sleep(10)

username_field = browser.find_element_by_name("session[username_or_email]")
password_field = browser.find_element_by_name("session[password]")
        
username_field.send_keys(username)
password_field.send_keys(password)
username_field.send_keys(Keys.RETURN)
time.sleep(10)

browser.get("https://twitter.com/settings/applications")
time.sleep(10)

#parent of span with 'Log out all...' text
browser.find_element_by_xpath("//*[contains(text(), 'Log out all other sessions')]/parent::*").click()

#confirm log out
browser.find_element_by_xpath("//div[@data-testid='confirmationSheetConfirm']")
