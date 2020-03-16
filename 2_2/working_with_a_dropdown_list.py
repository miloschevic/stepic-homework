from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome('C:/Chromedriver/chromedriver.exe')
browser.get('http://suninjuly.github.io/selects1.html')

def calc(a, b):
    return a + b

x1 = browser.find_element_by_id('num1').text
x2 = browser.find_element_by_id('num2').text

sum = calc(int(x1),int(x2))


select = Select(browser.find_element_by_tag_name('select'))
select.select_by_visible_text(str(sum))
browser.find_element_by_tag_name('button').click()
