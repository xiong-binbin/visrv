import requests
import json
from datetime import datetime


timeStr = datetime.now().strftime("%Y%m%d%H%M%S")
pUrl = 'http://127.0.0.1:5000/api/article'

pData = {
  "key": timeStr,
  "value": {
    "article": "流程规范",
    "menus": [
      {"index": 0, "name": "开发流程", "active": False, "items": [
        {"id": 0, "title": "定制项目开发", "link": "", "active": False,},
        {"id": 1, "title": "软件需求评估", "link": "", "active": False,},
        {"id": 2, "title": "软件任务实现", "link": "", "active": False,},
        {"id": 3, "title": "软件测试验证", "link": "", "active": False,},
        {"id": 4, "title": "定制需求变更", "link": "", "active": False,},
        {"id": 5, "title": "客诉问题解决", "link": "", "active": False,},
        ]},
      {"index": 1, "name": "指导规范", "active": False, "items": [
        {"id": 0, "title": "代码迁出规范", "link": "", "active": False,},
        {"id": 1, "title": "软件编码规范", "link": "", "active": False,},
        {"id": 2, "title": "缺陷解决规范", "link": "", "active": False,},
        {"id": 3, "title": "集成测试规范", "link": "", "active": False,},
        {"id": 4, "title": "测试提交规范", "link": "", "active": False,},
        {"id": 5, "title": "兼容性对照表", "link": "", "active": False,},
        {"id": 6, "title": "萤石需求对照表", "link": "", "active": False,},
        {"id": 7, "title": "制造需求对照表", "link": "", "active": False,},
        {"id": 8, "title": "需求评估指导书", "link": "", "active": False,},
        ]},
      {"index": 2, "name": "参考模板", "active": False, "items": [
        {"id": 0, "title": "用户需求模板", "link": "", "active": False,},
        {"id": 1, "title": "设计需求模板", "link": "", "active": False,},
        {"id": 2, "title": "概要设计模板", "link": "", "active": False,},
        {"id": 3, "title": "集成测试模板", "link": "", "active": False,},
        {"id": 4, "title": "更新说明模板", "link": "", "active": False,},
        {"id": 5, "title": "测试要点模板", "link": "", "active": False,},
        {"id": 6, "title": "生产说明模板", "link": "", "active": False,},
        {"id": 7, "title": "定制说明模板", "link": "", "active": False,},
        {"id": 8, "title": "会议纪要模板", "link": "", "active": False,},
        ]},
      {"index": 3, "name": "作业检查单", "active": False, "items": [
        {"id": 0, "title": "需求确认检查单", "link": "", "active": False,},
        {"id": 1, "title": "需求评估检查单", "link": "", "active": False,},
        {"id": 2, "title": "测试要点检查单", "link": "", "active": False,},
        {"id": 3, "title": "任务审核检查单", "link": "", "active": False,},
        {"id": 4, "title": "定制成果物清单", "link": "", "active": False,},
        {"id": 5, "title": "版本同步检查单", "link": "", "active": False,},
        ]},
      {"index": 4, "name": "日常工作规范", "active": False, "items": [
        {"id": 0, "title": "出差规范", "link": "", "active": False,},
        {"id": 1, "title": "请假规范", "link": "", "active": False,},
        {"id": 2, "title": "开会规范", "link": "", "active": False,},
        {"id": 3, "title": "工作交接", "link": "", "active": False,},
        {"id": 4, "title": "SVN权限申请", "link": "", "active": False,},
        ]},
    ],
  }
}

tmp = json.dumps(pData)
respond = requests.post(pUrl, data=tmp)
print(respond.text)