import requests
import json


pUrl = 'http://127.0.0.1:5000/api/page'

pData = {
  "key": "index",
  "value": {
    "article": {
      "list_0": [
        {"id": 0, "title": "article0", "link": "/article?id=20200915001916"},
      ],
      "list_1": [
        {"id": 0, "title": "article1", "link": "/article?id=20200915001921"},
      ],
      "list_2": [
        {"id": 0, "title": "article2", "link": "/article?id=20200915001913"},
      ],
      "list_3": [
        {"id": 0, "title": "article3", "link": "/article?id=20200915001907"},
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