from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()