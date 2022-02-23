import math
import os
from telnetlib import EC

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.CSS_SELECTOR, 'button[id="book"]').click()

    x = int(browser.find_element_by_id('input_value').text)
    answer_input = browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
