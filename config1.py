import os
version = 0.8554

server_name = "monitor"
server_port = 80
server_host = "localhost"
time_step = 1  # s
max_items_count = 40
fig_hw = 2
threaded=False  # set FLASK_TREADS
processes=3
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '999'



