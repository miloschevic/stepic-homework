import time
import math
from selenium import webdriver

driver = webdriver.Chrome('C:/Chromedriver/chromedriver.exe')

driver.get("http://suninjuly.github.io/math.html")


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

form = driver.find_element_by_id('answer')
form.send_keys(y)

option1 = driver.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()
option2 = driver.find_element_by_css_selector("[for='robotsRule']")
option2.click()

button = driver.find_element_by_css_selector("[class='btn btn-default']")
button.click()

driver.quit()
