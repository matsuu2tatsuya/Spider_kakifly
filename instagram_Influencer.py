# ig_hashtag_search?user_id=17841438910663891&q=韓国コスメ
# 17841563248081643/top_media?fields=caption,like_count,media_url,timestamp,comments_count,permalink,id&limit=50&user_id=17841438910663891

import requests
import json
import re
import csv
import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions

topMedia_List = []

influencer_name = []
influencer_sumPop = []
influencer_List = []
influencer_follower = []
influencer_sumPost = []

def selected_hashtags():
    print('検索したいハッシュタグ名を入力してください。')
    print('入力例/ #韓国コスメ => 韓国コスメ')
    hashtag = input(str())
    print('*' + hashtag + '*の人気の投稿を検索します。')
    print('-----------------------------------------')
    return hashtag

def get_hashtag_id(hashtag, token, kamikochi):
    instagram = requests.get(
        f'https://graph.facebook.com/v7.0/ig_hashtag_search?user_id={kamikochi}'
        f'&q={hashtag}&access_token={token}'
    ).json()
    hashtag_id = instagram["data"][0]['id']
    print('このハッシュタグのIDは' + hashtag_id + 'です。')
    return hashtag_id

def get_topMedia_by_hashtag(hashtag, token, kamikochi):
    instagram = requests.get(
        f'https://graph.facebook.com/v7.0/{hashtag}/'
        f'top_media?fields=caption,like_count,media_url,timestamp,comments_count,permalink,id'
        f'&limit=50&user_id={kamikochi}&access_token={token}'
    ).json()
    # print(json.dumps(instagram, indent=2, ensure_ascii=False))
    for i in instagram['data']:
        topMedia_List.append(i['permalink'])
    return instagram['paging']['next']

def get_next_by_hashtag(nextUrl):
    instagram = requests.get(nextUrl).json()
    for i in instagram['data']:
        topMedia_List.append(i['permalink'])
    return


def get_influencer_by_selenium(url):
    driver.get(url)
    username = driver.find_elements_by_css_selector(
        '#react-root > section > main > div > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > a')[
        0].get_attribute("textContent")
    userLink = f'https://www.instagram.com/{username}/'
    # print(userLink)
    influencer_List.append(userLink)
    print('thanks')
    return

def get_influencer_data_by_selenium(url):
    driver.get(url)

    try:
        follower = driver.find_elements_by_css_selector(
            '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span')[
            0].get_attribute("textContent")
        follower = re.sub(r',', '', follower)
        follower = re.sub(r'k', '000', follower)
        if '.' in follower:
            follower = re.sub(r'[.]', '', follower)
            follower = re.sub(r'0', '00', follower)
    except Exception:
        follower = 'Sorry'
    try:
        name = driver.find_elements_by_css_selector(
            '#react-root > section > main > div > header > section > div.-vDIg > h1')[
            0].get_attribute("textContent")
    except Exception:
        name = 'Sorry'

    try:
        sumPost = driver.find_elements_by_css_selector(
            '#react-root > section > main > div > header > section > ul > li:nth-child(1) > a > span')[
            0].get_attribute("textContent")
    except Exception:
        sumPost = 'Sorry'

    with open(f'{hashtag}.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(
            [f'{name}', f'{follower}', f'{sumPost}', f'{influencer_List.count(url)}', f'{url}'])

    print('okdesu')
    return


if __name__ == '__main__':
    """
    ハッシュタグごとに５０件人気の投稿（TopMedia）を取得する。
    人気の投稿とは、instagram公式でハッシュタグ検索したとき上位に表示されるものである。
    これは基本的にPV数とユーザーのインタラクションの組み合わせで決定される。
    ＊７日間で最大３０個の一意のハッシュタグを食えるすることができる。
    ＊ユーザー名など、個人の特定に関する情報が取得できないため、Seleniumで対処を狙う。
    """
    access_token = 'EAAKnCuyATroBAASs7SQAg9NdiZChumFZCHsf4s9e2l9XsAdpDv79PjGpFSPzM2kur6ixl9UyOH1zfIEuUhHarO0vlBZBCDu7Ocl1681Iw6DeeGEBpb62nIlygQJwwkKiJWAZCaHdqbwcPvMPRUHeg3YPNUOOouNCBmQWv5ITZCdbNqzXL9CmE'
    Kamikochi_ID = 17841432104009484
    hashtag = selected_hashtags()
    hashtag_id = get_hashtag_id(hashtag, access_token, Kamikochi_ID)
    nextUrl = get_topMedia_by_hashtag(hashtag_id, access_token, Kamikochi_ID)
    get_next_by_hashtag(nextUrl)
    print(topMedia_List)
    options = ChromeOptions()
    options.headless = True
    driver = Chrome(options=options)
    print('しばらくお待ちください。')
    print(len(topMedia_List))
    for i in topMedia_List:
        get_influencer_by_selenium(i)

    List = list(set(influencer_List))
    for i in List:
        get_influencer_data_by_selenium(i)

    driver.quit()

    df = pd.DataFrame(
        data={'influencer_name': influencer_name, 'influencer_List': influencer_List,
              'influencer_follower': influencer_follower, 'influencer_sumPost': influencer_sumPost},
        columns=['ユーザー名', 'permalink', 'フォロワー', '総投稿数']
    )
    df.to_csv(f'IG_influencer_{hashtag}.csv')
    print(df)
