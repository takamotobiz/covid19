import csv
import requests
from bs4 import BeautifulSoup

# 置換用のディクショナリ
nndict = {"North America":"","Europe":"","Asia":"","South America":"","Oceania":"","Africa":"","World":"","Total:":"","":""}
countrydict = {"USA":"United States of America","China":"People's Republic of China","UK":"United Kingdom","S. Korea":"South Korea","Czechia":"Czech Republic","UAE":"United Arab Emirates","North Macedonia":"Republic of Macedonia","DRC":"Democratic Republic of the Congo","CAR":"Central African Republic"}
columndict = {"CountryOther":"Country","TotalCases":"TCases","NewCases":"NCases","TotalDeaths":"TDeaths","NewDeaths":"NDeaths","TotalRecovered":"TRecovered","ActiveCases":"ACases","SeriousCritical":"Critical","Tot Cases/1M pop":"TC1Mpop","Deaths/1M pop":"D1Mpop","TotalTests":"TTests","Tests/1M pop":"T1Mpop"}

# URLの指定
target_url = "https://www.worldometers.info/coronavirus/#countries"
r = requests.get(target_url)

bsObj = BeautifulSoup(r.text, "html.parser")

# テーブルを指定
table = bsObj.findAll("table", {"class":"table table-bordered table-hover main_table_countries"})[0]
rows = table.findAll("tr")

with open("stat.csv", "w", encoding='utf-8',newline="") as file:
    writer = csv.writer(file,delimiter=",")
    for row in rows:
        csvRow = []
        for cell in row.findAll(['th']):
            # 項目内のカンマと改行を削除
            csvtext = cell.get_text().replace(",","").replace("\n","")
            # カラム名を置換
            csvRow.append(csvtext if csvtext not in columndict else columndict[csvtext])
        # セル位置を示すカウンター
        cellcnt = 0
        for cell in row.findAll(['td']):
            if cellcnt==1:
                # セルを取得
                csvtext = cell.get_text().replace("\n","")
                # 国名を置換
                csvRow.append(csvtext if csvtext not in countrydict else countrydict[csvtext])
            else:
                # セル内のカンマと改行を削除
                csvtext = cell.get_text().replace(",","").replace("\n","").replace(" ","").replace("+","").replace("N/A","")
                # 数値項目を置換
                csvRow.append(csvtext)
            # 次のセルへ
            cellcnt+=1
        if( csvRow[0] not in nndict ):
            writer.writerow(csvRow)
            print(csvRow)
