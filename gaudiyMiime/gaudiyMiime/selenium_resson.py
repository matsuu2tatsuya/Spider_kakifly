from selenium.webdriver import Chrome, ChromeOptions, Remote
from scrapy.http import HtmlResponse
import time

options = ChromeOptions()
options.headless = True
driver = Chrome(options=options)

driver.get('https://cryptospells.jp/trades')
time.sleep(0.5)
input_element = driver.find_element_by_xpath("//span[@class='checkmark']")
input_element.click()
time.sleep(0.5)
h = 0
r = []

while h < 100:
    driver.execute_script('scroll(0, document.body.scrollHeight)')
    r.append(len(driver.find_elements_by_css_selector('div.col-card')))
    print(r)
    h = h + 1
    print(h)
    if h == 100:
        print('BREEK')
        break
    if len(r) > 2:
        time.sleep(0.3)
        if r[-1] - r[-2] != 0 and r[-1] - r[-2] < 20:
            break

driver.quit()
