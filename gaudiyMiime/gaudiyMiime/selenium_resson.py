from selenium.webdriver import Chrome, ChromeOptions
import time

options = ChromeOptions()
# options.headless = True
driver = Chrome(options=options)
driver.implicitly_wait(20)

driver.get('https://gaudiy.com/community_details/avJEInz3EXlxNXKMSWxR')
time.sleep(0.3)
input_element = driver.find_element_by_css_selector('button:nth-child(5) > span > span > p')
if input_element:
    input_element.click()
time.sleep(0.3)
source_element = driver.find_element_by_css_selector('label.MuiFormControlLabel-root')
if source_element:
    source_element.click()
    time.sleep(1.0)
    link = driver.find_elements_by_css_selector('button > div > p:nth-child(1)')[3]
    driver.execute_script("arguments[0].scrollIntoView(true);", link)
    time.sleep(0.3)
    link = driver.find_elements_by_css_selector('button > div > p:nth-child(1)')[12]
    driver.execute_script("arguments[0].scrollIntoView(true);", link)
    time.sleep(0.3)
    link = driver.find_elements_by_css_selector('button > div > p:nth-child(1)')[21]
    driver.execute_script("arguments[0].scrollIntoView(true);", link)


print('全て表示されているはず。')

for res in driver.find_elements_by_css_selector('button > div > p:nth-child(1)'):
    print(res.get_attribute("textContent"))
for res in driver.find_elements_by_css_selector('button > div > p:nth-child(2)'):
    print(res.get_attribute("textContent"))
for res in driver.find_elements_by_css_selector('button > div > p:nth-child(3)'):
    print(res.get_attribute("textContent"))

driver.quit()
