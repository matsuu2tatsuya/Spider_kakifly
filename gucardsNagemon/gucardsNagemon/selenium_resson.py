from selenium.webdriver import Chrome, ChromeOptions
import time

options = ChromeOptions()
# options.headless = True
driver = Chrome(options=options)
driver.implicitly_wait(20)

driver.get('https://gu.cards/?marketplace=with_listings')

driver.execute_script('scroll(0, document.body.scrollHeight)')
input_element = driver.find_elements_by_css_selector(
    'body > div.cards-index.cards-hover.padding-top-small-fixed.position-relative > form > '
    'div.js-main-content.column.main-column.left-column-open.right-column-open.position-relative > '
    'div.pagination-wrapper.row.text-align-left.padding-top-tinys-fixed.padding-bottom-extra-small-fixed > div > a > '
    'div > div.button-center > div')[0]
input_element.click()

more_element = driver.find_elements_by_css_selector(
    'body > div.cards-index.cards-hover.padding-top-small-fixed.position-relative > form > '
    'div.js-main-content.column.main-column.left-column-open.right-column-open.position-relative > '
    'div.pagination-wrapper.row.text-align-left.padding-top-tinys-fixed.padding-bottom-extra-small-fixed > div > a > '
    'div > div.button-center > div')[1]

while more_element:
    # 二重クリック防止（今のURLが同じだとnextボタンをクリックしない）
    current = driver.current_url
    more_element = input_element = driver.find_elements_by_css_selector(
        'body > div.cards-index.cards-hover.padding-top-small-fixed.position-relative > form > '
        'div.js-main-content.column.main-column.left-column-open.right-column-open.position-relative > '
        'div.pagination-wrapper.row.text-align-left.padding-top-tinys-fixed.padding-bottom-extra-small-fixed > div > '
        'a > div > div.button-center > div')[1]
    time.sleep(0.5)
    if more_element:
        try:
            more_element.click()
            if current != driver.current_url:
                pass
        except Exception:
            break
    else:
        break

driver.quit()
