import redis
from err_raise import PoolEmptyError
from settings import REDIS__LIST_NAME, REDIS_HOST, REDIS_PASSWORD, REDIS_PORT


class RedisClient(object):
    """
    Redis连接类，用于连接Redis数据库并操纵其中的代理数据列表
    """
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT):
        """
        连接Redis数据库
        :param host: 数据库ip地址
        :param port: 数据库端口
        """
        if REDIS_PASSWORD:
            self._db = redis.Redis(host=host, port=port, password=REDIS_PASSWORD)
        else:
            self._db = redis.Redis(host=host, port=port)

    @property
    def list_len(self):
        """
        获取队列长度
        :return: 返回队列长度
        """
        return self._db.llen(REDIS__LIST_NAME)

    def flush(self):
        """
        清空队列
        """
        self._db.flushall()

    def get_for_test(self, num=1):
        """
        从Redis队列左端获取num个代理，用于测试有效性
        :param num: 一次性获取代理个数，默认值为1
        :return: 返回获取代理(bytes类型)构成的列表
        """
        proxies_to_get = self._db.lrange(REDIS__LIST_NAME, 0, num - 1)
        self._db.ltrim(REDIS__LIST_NAME, num, -1)
        return proxies_to_get

    def put(self, proxy):
        """
        向Redis队列右侧插入1个代理
        :param proxy: 插入的代理，类型为bytes
        """
        self._db.rpush(REDIS__LIST_NAME, proxy)

    def pop_for_use(self):
        """
        从Redis队列右端获取1个可用代理
        """
        try:
            return self._db.rpop(REDIS__LIST_NAME)
        except:
            raise PoolEmptyError
