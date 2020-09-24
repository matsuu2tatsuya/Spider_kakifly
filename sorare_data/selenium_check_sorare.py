from selenium.webdriver import Chrome, ChromeOptions, Remote

options = ChromeOptions()
driver = Chrome(options=options)
driver.get('https://www.soraredata.com/')

i = True
while i:
    driver.execute_script('scroll(0, document.body.scrollHeight)')
