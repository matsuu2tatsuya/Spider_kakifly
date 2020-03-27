from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.headless = True
driver = Chrome(options=options)
driver.implicitly_wait(10)

driver.get('https://gaudiy.com/community_details/avJEInz3EXlxNXKMSWxR')
input_element = driver.find_element_by_css_selector('div > button > div > svg')
input_element.click()
source_element = driver.find_element_by_css_selector('label.MuiFormControlLabel-root')
if source_element:
    source_element.click()
print('DEKETA')
driver.quit()
