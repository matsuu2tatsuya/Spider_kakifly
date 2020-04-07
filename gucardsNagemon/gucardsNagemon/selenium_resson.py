from selenium.webdriver import Chrome, ChromeOptions
import time

options = ChromeOptions()
options.headless = True
driver = Chrome(options=options)
driver.implicitly_wait(20)

driver.get('https://miime.io/assets/2')
input_element = driver.find_elements_by_css_selector(
    '#__layout > div > main > div.filterButtonBar > div > div:nth-child(5) > a')[0]
input_element.click()
time.sleep(0.5)
more_element = driver.find_element_by_css_selector('#__layout > div > main > div.assetCardList > '
                                                   'div.loadMoreButton__Container > div > '
                                                   'button.loadMoreButton')
while more_element:
    more_element = driver.find_element_by_css_selector('#__layout > div > main > div.assetCardList > '
                                                       'div.loadMoreButton__Container > div > '
                                                       'button.loadMoreButton')
    time.sleep(0.5)
    if more_element:
        try:
            more_element.click()
        except Exception:
            break
    else:
        break

driver.quit()
