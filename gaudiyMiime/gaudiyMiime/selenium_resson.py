from selenium.webdriver import Chrome, ChromeOptions
import time

options = ChromeOptions()
options.headless = True
driver = Chrome(options=options)
driver.implicitly_wait(30)

driver.get('https://cryptospells.jp/trades')
input_element = driver.find_element_by_xpath("//span[@class='checkmark']")
input_element.click()
h = 0
r = []

while h < 200:
    driver.execute_script('scroll(0, document.body.scrollHeight)')
    time.sleep(0.3)
    r.append(len(driver.find_elements_by_css_selector('div.col-card')))
    time.sleep(0.3)
    print(r)
    h = h + 1
    print(h)
    if h == 200:
        # print('BREEK')
        break
    if len(r) > 2:
        if r[-1] - r[-2] != 0 and r[-1] - r[-2] < 20:
            break
    if len(r) > 7:
        if r[-1] == r[-7]:
            break

driver.quit()
