from selenium.webdriver import Chrome, ChromeOptions
import time
import random
from selenium.webdriver.common.keys import Keys

options = ChromeOptions()
driver = Chrome(options=options)
driver.implicitly_wait(10)
driver.get('https://godsunchained.com/marketplace')

def singin():
    time.sleep(random.randrange(2, 4))
    email = driver.find_elements_by_css_selector("input.ng-untouched")[0]
    email.send_keys("ryoba666@sofia.re")
    time.sleep(random.randrange(2, 4))
    keypass = driver.find_elements_by_css_selector("input.ng-untouched")[1]
    keypass.send_keys("password")
    time.sleep(random.randrange(2, 4))
    Gologin = driver.find_element_by_css_selector("gu-primary-hex-button")
    Gologin.click()

singin()
time.sleep(random.randrange(2, 4))
driver.get(
    'https://godsunchained.com/marketplace/search?groupby=name&sortby=timestamp&orderby=desc&currentpage=1&perpage=300&assettype=card')

# time.sleep(5)
# driver.quit()


# def expand_shadow_element(element):
#     shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
#     return shadow_root
#
#
# root1 = driver.find_elements_by_css_selector('gu-login-form')[0]
# shadow_root1 = expand_shadow_element(root1)
#
# root2 = shadow_root1.find_element_by_css_selector('gu-form')
# shadow_root2 = expand_shadow_element(root2)
#
# search_button = shadow_root2.find_element_by_css_selector(".formControl")
#
# id = driver.find_elements_by_css_selector("input.inputArea__input")[0]
# id.send_keys("ryoba666@sofia.re")
# password = driver.find_elements_by_css_selector("input.inputArea__input")[1]
# password.send_keys("password")
