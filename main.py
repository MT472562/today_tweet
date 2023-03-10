#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import tweepy

text_url="https://kids.yahoo.co.jp/today/"

html=requests.get(text_url)
soup=BeautifulSoup(html.content, "html.parser")

text=soup.find("dd")
text=str(text)
text=text.replace('<dd>', '')
text=text.replace('</dd>', '')
text=text.replace('この日', '今日')

titl=soup.find("dt")
titl=str(titl)
titl=titl.replace('<dt>', '')
titl=titl.replace('</dt>', '')
titl=titl.replace('<span>', '')
titl=titl.replace('</span>', '')

day=soup.find("h2")
day=str(day)
day=day.replace('<h2 id="date">', '')
day=day.replace('<span class="date__dayW">', '')
day=day.replace('</h2>', '')
day=day.replace('<span>', '')
day=day.replace('</span>', '')
day=day.replace('\n', '')
tweettext=\
    "【{0}今日はなんの日？】".format(day)+"\n"\
        "今日は{0}".format(titl)+"\n\n"\
            "{0}".format(text)+"\n"\
                "今日も一日頑張りましょう！"
COSUMER_KEY = ''
COSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET =''
client = tweepy.Client(
consumer_key = COSUMER_KEY,
consumer_secret = COSUMER_SECRET,
access_token = ACCESS_TOKEN,
access_token_secret = ACCESS_TOKEN_SECRET
)
client.create_tweet(text=str(tweettext))
print(tweettext)
