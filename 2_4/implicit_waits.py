from selenium import webdriver

browser = webdriver.Chrome('C:/Chromedriver/chromedriver.exe')
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get('http://suninjuly.github.io/wait1.html')

button = browser.find_element_by_id('verify').click()
message = browser.find_element_by_id('verify_message')

assert 'successful' in message.text