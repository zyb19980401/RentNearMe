from bs4 import BeautifulSoup
from requests import get
import re
import csv
import pandas as pd
import sys
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)
htmlInput = sys.argv[1]

csv_file = open('condoData.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['price', 'address', 'bedRoomInfo', 'bathRoomInfo', 'parkingInfo', 'sizeInfo', 'link', 'fee'])

def getHouseInfo(houseTypeHtml):
    # a function that takes a house html and return a list that contains[bedroom Info, bathroom Info,Parking \\
    # Info, size Info]
    htmlAfterSplit = houseTypeHtml.split("<")
    resultInfo = []
    for houseinfo in htmlAfterSplit:
        if "BD" in houseinfo or "Studio" in houseinfo or "BA" in houseinfo or "Parking" in houseinfo or "sqft" in houseinfo:
            try:
                found = re.search('>.+', houseinfo).group(0)[1:]  # group 0 contains only matched string
                print(found)
                if found == "1 BD" or found == "1 BA" or found == "1 Parking":
                    found = 1
                elif found == "1+1 BD":
                    found = 1.5
                elif found == "2 BD" or found == "2 BA" or found == "2 Parking":
                    found = 2
                elif found == "0 Parking":
                    found = 0
                print(found)
            except AttributeError:
                found = ''
            resultInfo.append(found)
    return resultInfo


def getCondo(souptoscrap):
    house_containers = souptoscrap.find_all('div', class_="FrmWb")
    allHouseInThePage = []
    for unit in house_containers:
        #find each unit from the house_containers, we will scrap information from each unit block
        # print(unit)
        link = 'https://condos.ca' + str(unit.a['href'])
        address = str(unit.a['alt'])
        price = unit.find('div', class_="_2PKdn").text[1:]
        price = price.replace(",", "")
        if unit.find('div', class_= "YjyI8").text:
            fee = unit.find('div', class_= "YjyI8").text
        else:
            fee = "0"
        houseType = str(unit.find('div', class_="_3FIJA"))
        houseInfo = getHouseInfo(houseType)  # return a list in form of [bedroom Info, bathroom Info, size Info]
        if len(houseInfo) == 4:
            bedRoomInfo = houseInfo[0]
            bathRoomInfo = houseInfo[1]
            parkingInfo = houseInfo[2]
            sizeInfo = houseInfo[3]
        else:
            continue
        result = [price, address, bedRoomInfo, bathRoomInfo, parkingInfo, sizeInfo, link, fee]
        allHouseInThePage.append(result)
    return allHouseInThePage


def loadData(IsRent):
    headers = ({'User-Agent':
                    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    condoForSale = "https://condos.ca/toronto/condos-for-sale"
    condoForRent = "https://condos.ca/toronto/condos-for-rent"
    if(IsRent):
        nextPage = condoForRent
    else:
        nextPage = condoForSale
    # while nextPage is not None:
    for i in range(3):
        print("wttttfff")
        response = get(nextPage, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        # print(getCondo(soup))
        acc = getCondo(soup)
        for condo in acc:
            csv_writer.writerow(condo)
        nextPagesBar = soup.find('ul', class_="_3h0Z4")
        allLiInNextPages = nextPagesBar.findAll('li')
        for i in range(len(allLiInNextPages)):
            try:
                if i == len(allLiInNextPages) - 1:
                    print("we have reach the last page")
                    nextPage = None
                    break
                elif len(allLiInNextPages[i]['class']) > 1:
                    # print(allLiInNextPages[i])
                    # print(allLiInNextPages[i]['class'])
                    urlWithoutHttp = allLiInNextPages[i + 1].find('a', class_="_3uJE2")['href']
                    new_url = "https://condos.ca" + urlWithoutHttp
                    nextPage = new_url
                    # print(new_url)
                    break
            except AttributeError:
                print("an exception ")



if __name__ == "__main__":
    # execute only if run as a script
    print(htmlInput)
    splitedInput = htmlInput.split(",")
    print(splitedInput)
    RentOrBuyChoice = splitedInput[0]
    LimitUpper = splitedInput[1]
    LimitLower = splitedInput[2]
    address = splitedInput[3]
    bedRoomNum = splitedInput[4]
    washRommNum = splitedInput[5]
    ParkingInfo = splitedInput[6]

    loadData(True)
    rawdata = pd.read_csv("./condoData.csv")
    rawdata.to_sql("RawData", con=engine, if_exists='append', index=False)
    cc = engine.execute("SELECT * FROM RawData WHERE 1000<= price <=3000 AND bedRoomInfo = %s AND bathRoomInfo = %s AND parkingInfo = %s" % (bedRoomNum,washRommNum,ParkingInfo)).fetchall()
    print(cc)
    

    # Option = input("Do u want to rent or buy?: ")
    # if Option == "buy":
    #     print("Plz hold while we forming the csv file for ur data")
    #     loadData(False)
    # else:
    #     print("Plz hold while we forming the csv file for ur data")
    #     loadData(True)
    # rawdata = pd.read_csv("./condoData.csv")
    # UpperLimit = int(input("What is ur upper Limit on Price?: "))
    # LowerLimit = int(input("What is ur lower Limit on Price?: "))

    # csv_file = open('condoDataPrice.csv', 'w')
    # csv_writer = csv.writer(csv_file)
    # csv_writer.writerow(['price', 'address', 'bedRoomInfo', 'bathRoomInfo', 'parkingInfo', 'sizeInfo', 'link', 'fee'])

    # for i in range(rawdata.shape[0]):
    #     temp = rawdata.iloc[i]
    #     price = temp["price"]
    #     if LowerLimit <= int(price) <= UpperLimit:
    #         acc = rawdata.iloc[i].values.tolist()
    #         csv_writer.writerow(acc)
