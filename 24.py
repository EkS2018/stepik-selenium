from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
  browser = webdriver.Chrome()

  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  price= WebDriverWait(browser, 11).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

  browser.find_element_by_id("book").click()

  x = browser.find_element_by_id("input_value").text
  y = str(math.log(abs(12*math.sin(int(x)))))
  browser.find_element_by_id("answer").send_keys(y)
  browser.find_element_by_id("solve").click()

  assert "successful" in message.text

finally:
    time.sleep(7)
    browser.close()
    browser.quit()

