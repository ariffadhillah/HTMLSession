# # import requests
# # from bs4 import BeautifulSoup
# # # import csv

# # key = '1 & 1 HOME HEALTH, INC.'
# # location = 'united states'

# # url = 'https://www.bing.com/search?q=1+%26+1+HOME+HEALTH%2C+INC.&aqs=edge.0.69i59j0l2j69i59j0l5.371j0j4&FORM=ANAB01&PC=LCTS'

# # headers = {
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
# # }

# # req = requests.get(url, headers=headers)
# # soup = BeautifulSoup(req.text, 'html.parser')

# # item = soup.findAll('h2')
# # print(item)
# # # from requests_html import HTMLSession

# # # session = HTMLSession()

# # # key = '1 & 1 HOME HEALTH, INC.'
# # # location = 'united states'

# # # url = 'https://www.bing.com/search?q={key}.&aqs=edge.0.69i59j0l2j69i59j0l5.371j0j4&FORM=ANAB01&PC=LCTS'

# # # headers = {
# # #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
# # # }

# # # r = session.get(url, headers=headers)

# # # soup = BeautifulSoup(r.text, 'html.parser')
# # # print(soup)
# # # # item = r.html.find()

# # # # s = HTMLSession()

# # # # r = s.get(url)

# # # item = soup.html.find('#lgb_info')
# # # print(item)
# # # for title in item:
# # #     items = {
# # #         'title': title.text,
# # #         'link': title.absolute_links
# # #     } 
# # #     print(items)

# from requests_html import HTMLSession

# session = HTMLSession()

# def scrape_title(query):
#     r = session.get(f'https://www.bing.com/search?q={query}')
#     title = r.html.find('title', first=True).text
#     return title

# query = "1 & 1 HOME HEALTH, INC."
# title = scrape_title(query)
# print(title)

from requests_html import HTMLSession

session = HTMLSession()
url = "https://www.flipkart.com/search?q=REDMI&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

r = session.get(url)

products = r.html.xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]', first=True)

for item in products.absolute_links:
    print(item)
