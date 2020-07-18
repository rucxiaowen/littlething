import requests
import pprint
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
'''
'''
# 1.查询公司公告

searchkey ="会计估计变更"
notautosubmit=""
sdate ="2018-04-30" # 4月要写04，不能写4
edate ="2019-04-30"
isfulltext = "false"
sortName = "pubdate"
sortType = "desc"
pageNum = "1"
Time = []
name = []
code = []
title = []
sum = pd.DataFrame()
while True:
    url_search = rf'http://www.cninfo.com.cn/new/fulltextSearch/full?searchkey={searchkey}&' \
                 rf'sdate={sdate}&' \
                 rf'edate={edate}&' \
                 rf'isfulltext={isfulltext}&' \
                 rf'sortName={sortName}&' \
                 rf'sortType={sortType}&' \
                 rf'pageNum={pageNum}'
    search_str = requests.get(url_search,headers =headers).json()
    if search_str['announcements'] == None:
        break
    print(type(search_str))
    pprint.pprint(search_str)

    # 2.储存公告信息
    announcements_list = search_str['announcements']
    for i in announcements_list:
        Time.append(i['adjunctUrl'].split("/")[1])
        name.append(i['secName'])
        code.append(i['secCode'])
        title.append(i["announcementTitle"].replace("<em>",'').replace("</em>", ''))
    pageNum = str(int(pageNum)+1)

Dict = pd.DataFrame({"time":Time,"code":code,"company_name":name,"title":title})
# sum = pd.concat([sum,Dict],axis=0)
Dict.to_csv("1.csv",encoding="ansi")
