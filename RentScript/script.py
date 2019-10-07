from bs4 import BeautifulSoup
import requests
from requests import get
import re
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

condoforsale = "https://condos.ca/toronto/condos-for-sale"
response = get(condoforsale, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
house_containers = soup.find_all('div', class_="FrmWb")
print(house_containers[0])
temp = house_containers[0]





























# print(ccc)


# images = []
# for img in ccc.findAll('img'):
#     print(img)

# print(images)

info_list = []
# temp = house_containers[0]
# print(house_containers[0])
# print('https://condos.ca' + str(house_containers[0].a['href']))
# print(temp)



# images = []
# for img in soup.findAll('img'):
#     images.append(img.get('src'))

for unit in house_containers:
    link = 'https://condos.ca' + str(unit.a['href'])
    address = str(unit.a['alt'])
    # print(unit)

a = house_containers
# print(a)

# print(soup)
# print(response.text[:1000])
#
# https://condos.ca/toronto/quartz-spectra-75-queens-wharf-rd-85-queens-wharf-rd/unit-3908-C4600032
#
# https://condos.ca/toronto/43-eglinton-avenue-east-condos-43-eglinton-ave-e/unit-308-C4599686


tessst = "https://condos.ca/toronto/the-republic-south-tower-70-roehampton-ave/unit-221-C4600019"
response = get(tessst, headers=headers)
soupa = BeautifulSoup(response.text, 'lxml')
#
image_scr = [x['src'] for x in soupa.findAll('img')]
css_link = [x['href'] for x in soupa.findAll('link')]
scipt_src = []   ## Often times script doesn't have attributes 'src' hence need for try/except
def find_list_resources (tag, attribute,soup):
   list = []
   for x in soup.findAll(tag):
       try:
           list.append(x[attribute])
       except KeyError:
           pass
   return(list)


bb = find_list_resources('img',"src",soupa)
# print(bb)








condoforsale =  "https://condos.ca/toronto/the-republic-south-tower-70-roehampton-ave/unit-221-C4600019"
response = get(condoforsale, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

img_tags = soup.find_all('img')
print(soup)
urls = [img['src'] for img in img_tags]

# print(urls)

# for url in urls:
#     filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
#     with open(filename.group(1), 'wb') as f:
#         if 'http' not in url:
#             # sometimes an image source can be relative
#             # if it is provide the base url which also happens
#             # to be the site variable atm.
#             url = '{}{}'.format(site, url)
#         response = requests.get(url)
#         f.write(response.content)

