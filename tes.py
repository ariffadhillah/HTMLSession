# from requests_html import HTMLSession

# session = HTMLSession()
# # https://www.yelp.com/biz/1-heart-hospice-and-palliative-care-torrance
# def scrape_title(query):
#     r = session.get(f'https://www.yelp.com/biz/{query}', headers=headers )
#     title = r.html.xpath('//*[@id="main-content"]/div[1]/div/div[2]/div[1]/h1', first=True)
#     return title

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
# }
# query = "1 & 1 HOME HEALTH, INC."
# title = scrape_title(query)
# print(title)

# # http://dev.virtualearth.net/REST/v1/Locations/US/WA/98052/Redmond/1%20Microsoft%20Way?o=xml&key={BingMapsKey}

# # url 'http://dev.virtualearth.net/REST/v1/Locations/US/{adminDistrict}/{postalCode}/{locality}/{addressLine}?includeNeighborhood={includeNeighborhood}&include={includeValue}&maxResults={maxResults}&key={BingMapsKey}'


# import requests
# from bs4 import BeautifulSoup

# baseulr= 'https://www.flipkart.com'

# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
# }

# r = requests.get('https://www.flipkart.com/kitchen-cookware-serveware/pr?count=40&otracker=CLP_lhs&sid=upp&fm=neo%2Fmerchandising&iid=M_ffeb74dc-ec25-4cd3-b8de-6f87a2c8d8a1_1_372UD5BXDFYS_MC.4EYWRCGS3WUT&otracker=hp_rich_navigation_4_1.navigationCard.RICH_NAVIGATION_Home%7EKitchen%2B%2526%2BDining_4EYWRCGS3WUT&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_4_L1_view-all&cid=4EYWRCGS3WUT&page=1')

# soup = BeautifulSoup(r.content, 'lxml')

# productlist = soup.find_all('div', class_='_4ddWXP')

# productlinks = []

# for item in productlist:
#     for link in item.find_all('a', href=True):    
#         # print(link['href'])
#         productlinks.append(baseulr + link['href'])

# print(productlinks)


import pandas as pd
import requests
from bs4 import BeautifulSoup

baseulr= 'https://www.flipkart.com'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}

productlinks = set()
for x in range(1,35):
  
    r = requests.get(f'https://www.flipkart.com/kitchen-cookware-serveware/spray-bottle/pr?sid=upp%2C3at&otracker=categorytree&page={x}')

    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='_4ddWXP')
    for item in productlist:
        for link in item.find_all('a', href=True):    
            productlinks.add(baseulr + link['href'])

# print(productlinks)

# testlink = 'https://www.flipkart.com/aanya-set-of-3-pastry-brushes-silicon-flat-brush-pack-3-silicon-handle-material-fibre/p/itmfbdc9ayuktuus?pid=COBFBCGZBYSMYZEG&lid=LSTCOBFBCGZBYSMYZEG1BGLBP&marketplace=FLIPKART&store=upp&srno=b_19_741&otracker=nmenu_sub_Home%20%26%20Furniture_0_Kitchen%2C%20Cookware%20%26%20Serveware&iid=97c35f27-c622-43f8-9b92-8f2c53a984be.COBFBCGZBYSMYZEG.SEARCH&ssid=zkqe766lls0000001652615768757'

flipkartlist = []
for link in productlinks:
    r = requests.get(link, headers=header)
    soup = BeautifulSoup(r.content, 'lxml')
    try: 
        productName = soup.find('h1', class_='yhB1nd').text.strip()
    except:
        productName = ''

    try:
        salesprice = soup.find('div', class_='_30jeq3 _16Jk6d').text.strip()
    except:
        salesprice = ''

    try:
        price = soup.find('div', class_='_3I9_wc _2p6lqe').text.strip()
    except:
        price = ''
    try:
        description = soup.find('div', class_='_1mXcCf RmoJUa').text.strip()
    except:
        description =  ' '

    try:
        tdbrand = soup.find('td', text='Brand')
        brand = tdbrand.find_next_sibling('td').find('li').text
        # brand = soup.find('li', class_='_21lJbe').text.strip()
    except:
        brand = ''

    try:
        tdModelName = soup.find('td', text='Model Name')
        modelName = tdModelName.find_next_sibling('td').find('li').text
        # brand = soup.find('li', class_='_21lJbe').text.strip()
    except:
        modelName = ''
    try:
        tdmodelNumber = soup.find('td', text='Model Number')
        modelNumber = tdmodelNumber.find_next_sibling('td').find('li').text
        # brand = soup.find('li', class_='_21lJbe').text.strip()
    except:
        modelNumber = ''


    try:
        tdColor = soup.find('td', text='Color')
        color = tdColor.find_next_sibling('td').find('li').text
        # brand = soup.find('li', class_='_21lJbe').text.strip()
    except:
        color = ''


    try:
        tdType = soup.find('td', text='Type')
        type = tdType.find_next_sibling('td').find('li').text
        # brand = soup.find('li', class_='_21lJbe').text.strip()
    except:
        type = ''

    try:
        ranting = soup.find('div', class_='_2d4LTz').text.strip()
        # brand = soup.find('li', class_='_21lJbe').text.strip()
    except:
        ranting = ''

    flipkart = {
        'insert' : ' ',
        'kaka dukan': ' ',
        'Product Name': productName,
        'Sales price': salesprice,
        'Price': price,
        'Description' : description,
        'Brand': brand,
        'Model Name': modelName,
        'Model Number': modelNumber,
        'Color': color,
        'Type': type,
        'Rating': ranting,
        'Highlight': ' ',
        'Categry': ' ',
        'Product Link': ' ',
        'Image-src': ' ',
        'Image': ''
    }
        
    # print(flipkart)
    flipkartlist.append(flipkart)
    print('Saving:', flipkart['Product Name'])


df = pd.DataFrame(flipkartlist, columns=[ 'insert',
        'kaka dukan',
        'Product Name',
        'Sales price'
        'Price',
        'Description',
        'Brand',
        'Model Name',
        'Model Number',
        'Color',
        'Type',
        'Rating',
        'Highlight',
        'Categry',
        'Product Link',
        'Image-src',
        'Image' ])

df.to_csv('flipkart.csv', index=False)

df = pd.DataFrame(flipkartlist)
print(df.head(15))