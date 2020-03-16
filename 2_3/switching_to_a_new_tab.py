from selenium import webdriver
import math

browser = webdriver.Chrome('C:/Chromedriver/chromedriver.exe')
browser.get('http://suninjuly.github.io/redirect_accept.html')

button = browser.find_element_by_tag_name('button').click()

new_tab = browser.window_handles[1]
browser.switch_to.window(new_tab)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element_by_id('input_value').text
y = calc(x)

answer_form = browser.find_element_by_id('answer').send_keys(y)

submit = browser.find_element_by_css_selector('[type="submit"]').click()