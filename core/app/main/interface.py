import json
import redis
from datetime import datetime


redisClient = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True, password='1231')
# timeStr = datetime.now().strftime("%Y%m%d%H%M%S")

def get_page(name):
    tmp = redisClient.hget('page', name)
    if tmp == None:
        return 'error'
    else:
        return tmp

def post_page(data):
    tmp = json.loads(data)
    redisClient.hset('page', tmp['key'], json.dumps(tmp['value']))
    return 'ok'


def get_article(id):
    tmp = redisClient.hget('article', id)
    if tmp == None:
        return 'error'
    else:
        return tmp

def post_article(data):
    tmp = json.loads(data)
    redisClient.hset('article', tmp['key'], json.dumps(tmp['value']))
    return 'ok'


def get_document(id):
    tmp = redisClient.hget('document', id)
    if tmp == None:
        return 'error'
    else:
        return tmp

def post_document(data):
    tmp = json.loads(data)
    redisClient.hset('document', tmp['key'], tmp['value'])
    return 'ok'



