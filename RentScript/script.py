from bs4 import BeautifulSoup
import requests
from requests import get
import re
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

condoforsale = "https://condos.ca/toronto/condos-for-sale"
response = get(condoforsale, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')




#try to find all the url and store them in to a list
next_pages = soup.find('ul', class_="_3h0Z4")
next_page_links = next_pages.findAll('a', class_="_3uJE2")
allUrlInThePage = [link['href'] for link in next_page_links]
print(allUrlInThePage)
# for link in next_page_links:
#     a = link['href']
#     print(a)
    # address = str(unit.a['alt'])
    # temp = link.a['href']
    # print(temp)




# print (next_page.a["href"])
# print(next_page_link)





















house_containers = soup.find_all('div', class_="FrmWb")
info_list = []
def getHouseInfo(houseTypeHtml):
    # a function that takes a house html and return a list that contains[bedroom Info, bathroom Info,Parking \\
    # Info, size Info]
    htmlAfterSplit = houseTypeHtml.split("<")
    resultInfo = []
    for houseinfo in htmlAfterSplit:
        if "BD" in houseinfo or "Studio" in houseinfo or "BA" in houseinfo or "Parking" in houseinfo or "sqft" in houseinfo:
            try:
                found = re.search('>.+', houseinfo).group(0)[1:]  # group 0 contains only matched string
            except AttributeError:
                found = ''
            resultInfo.append(found)
    return resultInfo





for unit in house_containers:
    #find each unit from the house_containers, we will scrap information from each unit block
    # print(unit)
    link = 'https://condos.ca' + str(unit.a['href'])
    address = str(unit.a['alt'])
    price = unit.find('div', class_="_2PKdn")
    houseType = str(unit.find('div', class_="_3FIJA"))
    houseInfo = getHouseInfo(houseType)  # return a list in form of [bedroom Info, bathroom Info, size Info]
    # print(houseInfo)
    bedRoomInfo = houseInfo[0]
    bathRoomInfo = houseInfo[1]
    parkingInfo = houseInfo[2]
    sizeInfo = houseInfo[3]



    # print()
    # print(address)
    # print(link)
    # print(unit)
a = house_containers





# print(a)

# print(soup)
# print(response.text[:1000])
#
# https://condos.ca/toronto/quartz-spectra-75-queens-wharf-rd-85-queens-wharf-rd/unit-3908-C4600032
#
# https://condos.ca/toronto/43-eglinton-avenue-east-condos-43-eglinton-ave-e/unit-308-C4599686


# tessst = "https://condos.ca/toronto/the-republic-south-tower-70-roehampton-ave/unit-221-C4600019"
# response = get(tessst, headers=headers)
# soupa = BeautifulSoup(response.text, 'lxml')
# #
# image_scr = [x['src'] for x in soupa.findAll('img')]
# css_link = [x['href'] for x in soupa.findAll('link')]
# print(image_scr)
# print(css_link)
