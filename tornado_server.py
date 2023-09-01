from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.options import options, parse_command_line
from flask_app import flask_app
from tornado_config import *

options.log_file_prefix = tornado_config['log_file_prefix']
options.log_to_stderr = tornado_config['log_to_stderr']
options.logging = tornado_config['logging']
cert_path = tornado_config['cert_path']
https_cert_file = cert_path + tornado_config['https_cert_file']
https_key_file = cert_path + tornado_config['https_key_file']
parse_command_line()


if cert_path is None:
    flask_server = HTTPServer(WSGIContainer(flask_app))
else:
    flask_server = HTTPServer(
        WSGIContainer(flask_app),
        ssl_options={
            "certfile": https_cert_file,
            "keyfile": https_key_file
        },
    )

if __name__ == '__main__':
    print(flask_app.url_map)
    flask_server.listen(port=tornado_config['port'])  # 监听 8080 端口
    IOLoop.current().start()

