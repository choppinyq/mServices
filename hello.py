from tornado.web import Application
from tornado.ioloop import IOLoop

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        # 向客户端响应数据
        self.write('<h3>Hello</h3>')


if __name__ == '__main__':
    app = Application([('/',IndexHandler)])
    # 绑定端口
    app.listen('7000')

    # 启动Web
    print('starting ')
    IOLoop.current().start()