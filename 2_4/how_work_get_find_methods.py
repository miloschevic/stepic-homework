from selenium import webdriver
import time

browser = webdriver.Chrome('C:/Chromedriver/chromedriver.exe')
browser.get('http://suninjuly.github.io/wait1.html')

time.sleep(1)
button = browser.find_element_by_id('verify').click()
message = browser.find_element_by_id('verify_message')

assert 'successful' in message.text