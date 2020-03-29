from selenium.webdriver import Chrome, ChromeOptions
import time

options = ChromeOptions()
# options.headless = True
driver = Chrome(options=options)
driver.implicitly_wait(30)

driver.get('https://gaudiy.com/community_details/avJEInz3EXlxNXKMSWxR')
time.sleep(0.5)
input_element = driver.find_element_by_css_selector('button:nth-child(5) > span > span > p')
if input_element:
    input_element.click()
time.sleep(0.5)
source_element = driver.find_element_by_css_selector('label.MuiFormControlLabel-root')
while source_element:
    try:
        source_element.click()
        break
    except Exception:
        break

print('DEKETA')

print('全て表示されているはず。')
# driver.quit()
