from selenium.webdriver import Chrome, ChromeOptions
import time

options = ChromeOptions()
options.headless = True
driver = Chrome(options=options)

driver.get('https://miime.io/assets/2')
time.sleep(0.5)
input_element = driver.find_elements_by_css_selector('#__layout > div > main > div.filterButtonBar > div > div:nth-child(5) > a')[0]
input_element.click()
time.sleep(0.7)
driver.execute_script('scroll(0, document.body.scrollHeight)')
more_elements = driver.find_elements_by_css_selector('#__layout > div > main > div.assetCardList > div.loadMoreButton__Container > div > button.loadMoreButton')[0]
while more_elements:
    try:
        more_elements = driver.find_elements_by_css_selector(
            '#__layout > div > main > div.assetCardList > div.loadMoreButton__Container > div > button.loadMoreButton')[0]
    except IndexError:
        print('全部表示完了しました。')
        break
    more_elements.click()
    time.sleep(0.5)

print('DEKETA')
driver.quit()
