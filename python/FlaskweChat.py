import hashlib
from flask import Flask, request, render_template, jsonify, make_response
import time
import _elementtree as ET

app = Flask(__name__)
app.debug = True


@app.route('/weixin/', methods=['GET', 'POST'])
def wechat_auth():
    if request.method == 'GET':
        token = '****'  # your token
    query = request.args
    signature = query.get('signature', '')
    timestamp = query.get('timestamp', '')
    nonce = query.get('nonce', '')
    echostr = query.get('echostr', '')
    s = [timestamp, nonce, token]
    s.sort()
    s = ''.join(s)
    if hashlib.sha1(s).hexdigest() == signature:
        return make_response(echostr)  