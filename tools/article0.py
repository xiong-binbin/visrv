import requests
import json
from datetime import datetime


timeStr = datetime.now().strftime("%Y%m%d%H%M%S")
pUrl = 'http://127.0.0.1:5000/api/article'

pData = {
  "key": timeStr,
  "value": {
    "article": "项目开发",
    "menus": [
      {"index": 0, "name": "接口人", "active": False, "items": [
        {"id": 0, "title": "设备软件", "link": "", "active": False,},
        {"id": 1, "title": "产品售前", "link": "", "active": False,},
        {"id": 2, "title": "技术支持", "link": "", "active": False,},
        {"id": 3, "title": "平台接口人", "link": "", "active": False,},
        {"id": 4, "title": "资源组接口", "link": "", "active": False,},
        ]},
      {"index": 1, "name": "实时进展", "active": False, "items": [
        {"id": 0, "title": "工作成员", "link": "", "active": False,},
        {"id": 1, "title": "工作组长", "link": "", "active": False,},
        {"id": 2, "title": "项目经理", "link": "", "active": False,},
        ]},
      {"index": 2, "name": "开发评估", "active": False, "items": [
        {"id": 0, "title": "准入条件", "link": "", "active": False,},
        {"id": 1, "title": "开发周期", "link": "", "active": False,},
        {"id": 2, "title": "提交材料", "link": "", "active": False,},
        {"id": 3, "title": "申请单填写", "link": "", "active": False,},
        {"id": 4, "title": "不支持的定制", "link": "", "active": False,},
        ]},
      {"index": 3, "name": "功能开发", "active": False, "items": [
        {"id": 0, "title": "通话逻辑", "link": "", "active": False,},
        {"id": 1, "title": "界面修改", "link": "", "active": False,},
        {"id": 2, "title": "SDK接入", "link": "", "active": False,},
        {"id": 3, "title": "萤石接入", "link": "", "active": False,},
        {"id": 4, "title": "云眸接入", "link": "", "active": False,},
        {"id": 5, "title": "声音合成", "link": "", "active": False,},
        {"id": 6, "title": "字库增删", "link": "", "active": False,},
        {"id": 7, "title": "数据库增删", "link": "", "active": False,},
        {"id": 8, "title": "多语言开发", "link": "", "active": False,},
        ]},
    ],
  }
}

tmp = json.dumps(pData)
respond = requests.post(pUrl, data=tmp)
print(respond.text)