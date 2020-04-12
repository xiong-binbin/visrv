import requests
import json


pUrl = 'http://127.0.0.1:5000/api/page'

pData = {
  "key": "index",
  "value": {
    "article": {
      "list_0": [
        {"id": 0, "title": "项目开发", "link": "/article?id=20200412220625"},
      ],
      "list_1": [
        {"id": 0, "title": "流程规范", "link": "/article?id=20200412220622"},
      ],
      "list_2": [
        {"id": 0, "title": "产品信息", "link": "/article?id=20200412220631"},
      ],
      "list_3": [
        {"id": 0, "title": "技术资料", "link": "/article?id=20200412220600"},
      ],
      "list_4": [
      ],
      "list_5": [
      ],
    },
  }
}

tmp = json.dumps(pData)
respond = requests.post(pUrl, data=tmp)
print(respond.text)