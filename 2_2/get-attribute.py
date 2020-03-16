import time, math
from selenium import webdriver

try:
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

    people_radio = driver.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    button = driver.find_element_by_css_selector("[class='btn btn-default']")
    button.click()

finally:
    driver.quit()
