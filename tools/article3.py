import requests
import json
from datetime import datetime


timeStr = datetime.now().strftime("%Y%m%d%H%M%S")
pUrl = 'http://127.0.0.1:5000/api/article'

pData = {
  "key": timeStr,
  "value": {
    "article": "技术资料",
    "menus": [
      {"index": 0, "name": "常见方案", "items": [
        {"id": 0, "title": "二维码开门", "link": "",},
        {"id": 1, "title": "蓝牙开门", "link": "",},
        {"id": 2, "title": "梯控呼梯", "link": "",},
        {"id": 3, "title": "业主互访", "link": "",},
        ]},
      {"index": 1, "name": "对外协议", "items": [
        {"id": 0, "title": "梯控协议", "link": "",},
        {"id": 1, "title": "智能家居", "link": "",},
        {"id": 2, "title": "SDK接入", "link": "",},
        ]},
      {"index": 2, "name": "专业资料", "items": [
        {"id": 0, "title": "IC卡", "link": "",},
        {"id": 1, "title": "SIP协议", "link": "",},
        {"id": 2, "title": "Jpeg格式", "link": "",},
        {"id": 3, "title": "MiniGUI", "link": "",},
        {"id": 4, "title": "SQL语句", "link": "",},
        {"id": 5, "title": "Linux命令", "link": "",},
        {"id": 6, "title": "性能优化", "link": "",},
        ]},
      {"index": 3, "name": "问题排查", "items": [
        {"id": 0, "title": "串口命令", "link": "",},
        {"id": 1, "title": "SSH登陆", "link": "",},
        {"id": 2, "title": "呼叫失败", "link": "",},
        {"id": 3, "title": "刷卡失败", "link": "",},
        {"id": 4, "title": "下发卡片失败", "link": "",},
        {"id": 5, "title": "下发人脸指纹失败", "link": "",},
        ]},
    ],
  }
}

tmp = json.dumps(pData)
respond = requests.post(pUrl, data=tmp)
print(respond.text)