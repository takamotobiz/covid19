# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select

import tkinter as tk
from tkinter import messagebox

options = webdriver.ChromeOptions()
# options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/14.4.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]')
options.add_argument(' --incognito')

# create chrome driver
driver = webdriver.Chrome(executable_path="./chromedriver", options=options)

# 緯度、経度、緯度・経度の誤差(単位：m)を設定する
driver.execute_cdp_cmd(
    "Emulation.setGeolocationOverride",
    {
        "latitude": 43.068864361601086,
        "longitude": 141.35110934983274,
        "accuracy": 100,
    },
)

# request URL
driver.get('https://www.google.co.jp/search?q=ランチ&ei=Yhw7XdqhNdn6-Qb_5bvABg&start=0&sa=N&ved=0ahUKEwja2o6v89LjAhVZfd4KHf_yDmg4FBDy0wMIdQ&biw=1920&bih=910')

# scroll footer
# 画面スクロールが不要であれば下記2行を削除してください。
# element = driver.find_element_by_id("sfooter")
# driver.execute_script("arguments[0].scrollIntoView(false);", element)

# hide root window
root = tk.Tk()
root.withdraw()
# show dialog( elapsed time(S) )
messagebox.showinfo("確認", "\"現在地を更新\"をクリックしOKボタンをクリックしてください")

# add case - quit Chrome
try:
    html = driver.page_source
    with open('001.html', 'w', encoding='utf-8') as f:
        f.write(html)

    driver.quit()
except:
    pass