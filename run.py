#  创建应用实例
# import sys

# from wxcloudrun import app

#  启动Flask Web服务
# if __name__ == '__main__':
#     app.run(host=sys.argv[1], port=sys.argv[2])

import sys
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run(host=sys.argv[1], port=sys.argv[2])
