from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium import webdriver


browser = webdriver.Chrome("C:/Chromedriver/chromedriver.exe")
browser.get('http://suninjuly.github.io/explicit_wait2.html')

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)

button_book = browser.find_element_by_id('book').click()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_elem = browser.find_element_by_id("input_value")
x = x_elem.text
y = calc(x)

form = browser.find_element_by_id("answer")
form.send_keys(y)

button_solve = browser.find_element_by_id('solve').click()




