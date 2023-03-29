from requests_html import HTMLSession

session = HTMLSession()
url = 'https://weedmaps.com/dispensaries/in/united-states/washington-dc'

s = HTMLSession()
r = s.get(url)

products = r.html.xpath('//*[@id="content"]/div/div[2]/div[1]/div/div[2]/div[3]/div/ul', first=True)
for item in products.absolute_links:
    print(item)