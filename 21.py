from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.find_element_by_tag_name("button").click()
    #confirm = browser.switch_to.alert
    #confirm.accept()

    windows = browser.window_handles
    current_window = browser.current_window_handle

    for win in windows:
        if current_window == win:
            print(win, " with current index: ", windows.index(win))
        else:
            print(win, " with index: ", windows.index(win))
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    print(x)
    y = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(7)
    browser.close()
    browser.quit()

