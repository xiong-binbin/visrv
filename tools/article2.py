import requests
import json
from datetime import datetime


timeStr = datetime.now().strftime("%Y%m%d%H%M%S")
pUrl = 'http://127.0.0.1:5000/api/article'

pData = {
  "key": timeStr,
  "value": {
    "article": "产品信息",
    "menus": [
      {"index": 0, "name": "产品型号", "active": False, "items": [
        {"id": 0, "title": "命名规范", "link": "", "active": False,},
        {"id": 1, "title": "国内型号", "link": "", "active": False,},
        {"id": 2, "title": "海外型号", "link": "", "active": False,},
        ]},
      {"index": 1, "name": "产品参数", "active": False, "items": [
        {"id": 0, "title": "数字室内机", "link": "", "active": False,},
        {"id": 1, "title": "模拟室内机", "link": "", "active": False,},
        {"id": 2, "title": "单元门口机", "link": "", "active": False,},
        {"id": 3, "title": "别墅门口机", "link": "", "active": False,},
        {"id": 4, "title": "数字门铃机", "link": "", "active": False,},
        {"id": 5, "title": "数字管理机", "link": "", "active": False,},
        {"id": 6, "title": "辅助类设备", "link": "", "active": False,},
        ]},
      {"index": 2, "name": "海外基线", "active": False, "items": [
        {"id": 0, "title": "EN_V1.4.5", "link": "", "active": False,},
        {"id": 1, "title": "EN_V1.4.62", "link": "", "active": False,},
        {"id": 2, "title": "EN_V1.5.0", "link": "", "active": False,},
        {"id": 3, "title": "EN_V1.5.1", "link": "", "active": False,},
        {"id": 4, "title": "EN_V2.0.0", "link": "", "active": False,},
        {"id": 5, "title": "EN_V2.0.2", "link": "", "active": False,},
        ]},
      {"index": 3, "name": "国内基线", "active": False, "items": [
        {"id": 0, "title": "CN_V1.4.25", "link": "", "active": False,},
        {"id": 1, "title": "CN_V1.4.26", "link": "", "active": False,},
        {"id": 2, "title": "CN_V1.4.27", "link": "", "active": False,},
        {"id": 3, "title": "CN_V1.4.46", "link": "", "active": False,},
        {"id": 4, "title": "CN_V2.0.0", "link": "", "active": False,},
        {"id": 5, "title": "CN_V2.0.1", "link": "", "active": False,},
        ]},
      {"index": 4, "name": "对讲产品", "active": False, "items": [
        {"id": 0, "title": "室内机", "link": "", "active": False,},
        {"id": 1, "title": "门口机", "link": "", "active": False,},
        {"id": 2, "title": "门铃机", "link": "", "active": False,},
        {"id": 3, "title": "管理机", "link": "", "active": False,},
        {"id": 4, "title": "套装产品", "link": "", "active": False,},
        {"id": 5, "title": "其他对讲产品", "link": "", "active": False,},
        ]},
      {"index": 5, "name": "门禁产品", "active": False, "items": [
        {"id": 0, "title": "门禁主机", "link": "", "active": False,},
        {"id": 1, "title": "读卡器", "link": "", "active": False,},
        {"id": 2, "title": "一体机", "link": "", "active": False,},
        {"id": 3, "title": "发卡器", "link": "", "active": False,},
        {"id": 4, "title": "智能身份识别", "link": "", "active": False,},
        {"id": 5, "title": "其他门禁产品", "link": "", "active": False,},
        ]},
    ],
  }
}

tmp = json.dumps(pData)
respond = requests.post(pUrl, data=tmp)
print(respond.text)