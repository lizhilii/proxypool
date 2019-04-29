# Redis数据库服务
REDIS_HOST = '127.0.0.1'          # 此处填写redis服务host地址
REDIS_PORT = 6379
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']    # 若有密码，则填写；若无则保持空
REDIS__LIST_NAME = "proxies"    # 可自定义队列名称

# Flask服务
FLASK_HOST = '0.0.0.0'          # '0.0.0.0'代表其他主机可以通过地址访问该接口
FLASK_PORT = 5000
DEBUG = True

# HTTP请求头
User_Agent = ''                 # 可以使用自己的User-Agent
HEADERS = {
    'User-Agent' : User_Agent,
}

# 代理测试网址
TEST_API = 'http://www.baidu.com'
# 代理测试时间上限
GET_PROXIES_TIMEOUT = 5

# 代理有效性检查周期(s)
VALID_CHECK_CYCLE = 60
# 代理池ip数量检查周期(s)
POOL_LEN_CHECK_CYCLE = 20
# 代理池ip数量上限
POOL_UPPER_THRESHOLD = 150
# 代理池ip数量下限
POOL_LOWER_THRESHOLD = 30