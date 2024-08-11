# 导入库
# schedule：用于安排定时任务。
# datetime：用于处理日期和时间。
# requests：用于发送 HTTP 请求。
# time：用于处理时间相关的操作。
# re：用于正则表达式处理（在这段代码中未使用）
# re库可以配和sever酱进行微信通知约座结果，觉得用处不大，删了
import schedule
import datetime
import requests
import time
import re

def job():
    t = ((datetime.datetime.now() ++datetime.timedelta(days = 1)
).strftime("%Y-%m-%d"))
    print(t)
# 设置请求头和请求数据，用于模拟浏览器请求。
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
    'seatNum': '1112',
}
    # json_data1 是要发送的 JSON 数据。
    # 它包含了某个实验室预约的信息，比如申请日期、开始时间、持续时间、房间 ID 和座位号。
    response1 = requests.post(
    'https://mipservice.tit.edu.cn/consumeServer/ReadingRoomWx/userSchLabApply',
    headers = headers, json =
    json_data1)
    print(response1.text)
# 使用 requests.post 发送 POST 请求，URL 指向一个实验室预约的接口。
# response1.text 打印请求的返回内容。
    

schedule.every().day.at("00:00").do(job)  #设置任务的运行时间 

while True: schedule.run_pending()
time.sleep(1)
