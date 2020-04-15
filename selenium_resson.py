from selenium.webdriver import Chrome, ChromeOptions
import time

options = ChromeOptions()
driver = Chrome(options=options)

driver.get(f'https://tokentrove.com/GodsUnchainedCards?page=1&perPage=120')
driver.execute_script('scroll(0, document.body.scrollHeight)')
driver.find_elements_by_css_selector('div.listing-wrapper')

driver.quit()
