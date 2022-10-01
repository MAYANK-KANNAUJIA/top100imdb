import urllib.request as url
import bs4
path=r"https://www.imdb.com/list/ls055592025/"
response=url.urlopen(path)
page=bs4.BeautifulSoup(response,"lxml")
title=page.find_all("a",{"href": "/title/tt0068646/?ref_=ttls_li_tt"})
rating=page.find_all("span",{"class":"ipl-rating-star__rating"})
for i in range(10):
    print(title[i].text)
    print(rating[i].text)
    print("*"*15)
