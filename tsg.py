import schedule
import datetime
import requests
import time
import re

def job():
    t = ((datetime.datetime.now() ++datetime.timedelta(days = 1)
).strftime("%Y-%m-%d"))
    print(t)
    headers = {
    'authority': 'mipservice.tit.edu.cn',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #Already added when you pass json = #
    'content-type': 'application/json',
    'origin': 'https://mipweb.tit.edu.cn',
    'referer': 'https://mipweb.tit.edu.cn/',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',

}
    json_data1 = {
    'cardNumber': '学号',
    'applyDate': t,
    'applyStartTime': '06:30',
    'applyDuration': '15.5',
    'labRoomId': '10',
    'seatNum': '座位号',
}
    response1 = requests.post(
    'https://mipservice.tit.edu.cn/consumeServer/ReadingRoomWx/userSchLabApply',
    headers = headers, json =
    json_data1)
    print(response1.text)
    

schedule.every().day.at("00:00").do(job)

while True: schedule.run_pending()

time.sleep(1)
