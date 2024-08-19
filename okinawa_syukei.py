#s24001
#沖縄県の推定人口のページより最新情報をスワッピングするpytonコード
#https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html

import requests
from bs4 import BeautifulSoup

uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

html.encoding = 'Shift_JIS'

#print(html.text)

soup = BeautifulSoup(html.text, "html.parser")
print(soup.find('title').string)

table = soup.find("table", class_="table1 font2 gyo5")
