from selenium import webdriver
import math

browser = webdriver.Chrome('C:/Chromedriver/chromedriver.exe') # указываем местоположение драйвера браузера
browser.get('https://suninjuly.github.io/execute_script.html') # открываем страницу в браузере

def calc(x):                                                # объявляем функцию высчитывающую значение х
    return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element_by_id('input_value').text          # находим значение х на странице
# Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента.
y = calc(x)                                                 # высчитываем значение

form = browser.find_element_by_id('answer')                 # находим форму для ввода ответа
form.send_keys(y)                                           # передаём ей ответ

button = browser.find_element_by_tag_name('button')         # находим кнопку
browser.execute_script("return arguments[0].scrollIntoView(true);", button) # прокручиваем страницу до кнопки

option1 = browser.find_element_by_id('robotCheckbox')
option1.click()

option2 = browser.find_element_by_id('robotsRule')
option2.click()

button.click()