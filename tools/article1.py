import requests
import json
from datetime import datetime


timeStr = datetime.now().strftime("%Y%m%d%H%M%S")
pUrl = 'http://127.0.0.1:5000/api/article'

pData = {
  "key": timeStr,
  "value": {
    "article": "article0",
    "menus": [
      {"index": 0, "name": "menu0", "active": False, "items": [
        {"id": 0, "title": "item0", "link": "", "active": False,},
        {"id": 1, "title": "item1", "link": "", "active": False,},
        {"id": 2, "title": "item2", "link": "", "active": False,},
        {"id": 3, "title": "item3", "link": "", "active": False,},
        {"id": 4, "title": "item4", "link": "", "active": False,},
        ]},
      {"index": 1, "name": "menu1", "active": False, "items": [
        {"id": 0, "title": "item0", "link": "", "active": False,},
        {"id": 1, "title": "item1", "link": "", "active": False,},
        {"id": 2, "title": "item2", "link": "", "active": False,},
        ]},
      {"index": 2, "name": "menu2", "active": False, "items": [
        {"id": 0, "title": "item0", "link": "", "active": False,},
        {"id": 1, "title": "item1", "link": "", "active": False,},
        {"id": 2, "title": "item2", "link": "", "active": False,},
        {"id": 3, "title": "item3", "link": "", "active": False,},
        {"id": 4, "title": "item4", "link": "", "active": False,},
        ]},
      {"index": 3, "name": "menu3", "active": False, "items": [
        {"id": 0, "title": "item0", "link": "", "active": False,},
        {"id": 1, "title": "item1", "link": "", "active": False,},
        {"id": 2, "title": "item2", "link": "", "active": False,},
        {"id": 3, "title": "item3", "link": "", "active": False,},
        {"id": 4, "title": "item4", "link": "", "active": False,},
        {"id": 5, "title": "item5", "link": "", "active": False,},
        ]},
    ],
  }
}

tmp = json.dumps(pData)
respond = requests.post(pUrl, data=tmp)
print(respond.text)