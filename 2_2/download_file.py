from selenium import webdriver
import os

browser = webdriver.Chrome('C:/Chromedriver/chromedriver.exe')
browser.get('https://suninjuly.github.io/file_input.html')

form_1 = browser.find_element_by_name('firstname')
form_1.send_keys('Ильдар')

form_2 = browser.find_element_by_name('lastname')
form_2.send_keys('Шамсутдинов')

form_3 = browser.find_element_by_name('email')
form_3.send_keys('test@test.com')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

element = browser.find_element_by_id('file')
element.send_keys(file_path)

button = browser.find_element_by_tag_name('button')
button.click()