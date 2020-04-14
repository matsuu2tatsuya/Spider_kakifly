from selenium.webdriver import Chrome, ChromeOptions
import time

options = ChromeOptions()
options.headless = True
driver = Chrome(options=options)
driver.implicitly_wait(20)

driver.get('https://www.nagemon.com/assets/sell')
input_element = driver.find_elements_by_css_selector('li > div.item')[14]
input_element.click()
for _ in range(10):
    driver.execute_script('scroll(0, document.body.scrollHeight)')
    time.sleep(0.5)

driver.quit()
