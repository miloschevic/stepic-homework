import math
from selenium import webdriver

driver = webdriver.Chrome('C:/Chromedriver/chromedriver.exe')

driver.get("https://suninjuly.github.io/get_attribute.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = driver.find_element_by_id('treasure')
x = x_element.get_attribute('valuex')
y = calc(x)

form = driver.find_element_by_id('answer')
form.send_keys(y)

option1 = driver.find_element_by_id("robotCheckbox")
option1.click()
option2 = driver.find_element_by_id('robotsRule')
option2.click()

button = driver.find_element_by_css_selector("[class='btn btn-default']")
button.click()

driver.quit()