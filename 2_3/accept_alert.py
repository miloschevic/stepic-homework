from selenium import webdriver
import math

browser = webdriver.Chrome('C:/Chromedriver/chromedriver.exe')
browser.get('https://suninjuly.github.io/alert_accept.html')

button = browser.find_element_by_tag_name('button')
button.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element_by_id('input_value').text
y = calc(x)

answer_form = browser.find_element_by_id('answer')
answer_form.send_keys(y)

submit = browser.find_element_by_css_selector('[type="submit"]')
submit.click()
