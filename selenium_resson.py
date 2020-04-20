from selenium.webdriver import Chrome, ChromeOptions
import re
import time

options = ChromeOptions()
driver = Chrome(options=options)

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
    link = driver.find_elements_by_css_selector('button > div > p:nth-child(1)')[-2]
    driver.execute_script("arguments[0].scrollIntoView(true);", link)
    time.sleep(0.3)
    while link != driver.find_elements_by_css_selector('button > div > p:nth-child(1)')[-2]:
        link = driver.find_elements_by_css_selector('button > div > p:nth-child(1)')[-2]
        driver.execute_script("arguments[0].scrollIntoView(true);", link)
        time.sleep(0.3)
