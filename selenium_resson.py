# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException

def check_coupon(driver, my_favorite_brand):
    i = 1
    while True:
      try:
          coupon_brand = driver.find_element_by_xpath(f'//*[@id="body"]/div[3]/ul/li[{i}]/a/figure/div[2]').text
          my_favorite_brand = driver.find_elements_by_css_selector('div.shopH')[1].get_attribute("textContent")
          if coupon_brand == my_favorite_brand:
              return True
          i += 1
      except NoSuchElementException:
          return False

if __name__ == '__main__':
    try:
        # Headless Chromeの設定
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument('--window-size=1420,1080')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # Headless Chromeブラウザに接続
        driver = webdriver.Chrome(options=options)
        # seleniumの動作タイムアウトを15秒間に設定
        driver.implicitly_wait(15)

        # ZOZOのクーポンページに遷移
        driver.get("https://zozo.jp/coupon/")
        # 好きなブランド
        my_favorite_brand = driver.find_elements_by_css_selector('div.shopH')[1].get_attribute("textContent")
        # クーポンのチェック
        if check_coupon(driver, my_favorite_brand):
            print("見つけたよ！ ", my_favorite_brand)
        else:
            print("今日は見つけられなかった・・・")

    # 例外処理
    except ElementClickInterceptedException as ecie:
        print(f"exception!\n{ecie}")
    except TimeoutException as te:
        print(f"timeout!\n{te}")
    finally:
        # 終了
        driver.close()
        driver.quit()
