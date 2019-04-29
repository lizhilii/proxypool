from flask import Flask, g
from db import RedisClient
from settings import FLASK_HOST, FLASK_PORT

# __all__ = ['app']
app = Flask(__name__)

def get_conn():
    """
    建立Redis连接；若已连接则直接返回
    :return: 返回一个Redis连接类的全局对象
    """
    if not hasattr(g, 'redis_client'):
        g.redis_client = RedisClient()
    return g.redis_client

@app.route('/')
def get_proxy():
    """
    打印代理队列的第一个数据
    """
    conn = get_conn()
    return conn.pop_for_use()

@app.route('/count')
def get_counts():
    """
    打印列表队列的长度
    """
    conn = get_conn()
    return str(conn.list_len)
