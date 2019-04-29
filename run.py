from api import app
from scheduler import Scheduler
from settings import FLASK_HOST, FLASK_PORT

def main():
    s = Scheduler()
    s.run()
    # Flask服务默认只能在本机进行连接，
    # 若需要远程访问，必须手动设置app.run()的host和port参数！
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=True)

if __name__ == '__main__':
    main()