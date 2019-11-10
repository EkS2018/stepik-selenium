from selenium import webdriver
import time
import os
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.find_element_by_css_selector("button.btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(7)
    browser.close()
    browser.quit()

