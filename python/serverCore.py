# coding=utf-8

html = '''True'''

import socket
import signal
import errno
import re
import hashlib

wxtoken = 'weixin'


def checksignature(pams):
    global wxtoken
    #加密签名
    signature = pams['signature']
    #微信时间戳
    timestamp = pams['timestamp']
    #随机数
    nonce = pams["nonce"];
    #连接字符串
    tmparr = [wxtoken, timestamp, nonce]
    #字典排序
    tmparr.sort()
    #在每个元素中间加入空格
    tmpstr = ''.join(tmparr)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    return tmpstr == signature


def checksignatureresponse(pams):
    if checksignature(pams):
        #随机字符串
        return pams['echostr']
    else:
        return ''


def app(data):
    s = data
    pams = dict(re.findall('([^=, ^&, ^?]*)=([^=, ^&]*)', s))
    return checksignatureresponse(pams)


def get_str(data):
    pattern = re.compile('&echostr=[\d]*×')
    res = pattern.findall(data)
    return res[0]


def HttpResponse(header, data):
    context = ''.join(app(data))
    response = "%s %d\n\n%s\n\n" % (header, len(context), context)
    return response


def sigIntHander(signo, frame):
    print('get signo# ', signo)
    global runflag
    runflag = False
    global lisfd
    lisfd.shutdown(socket.SHUT_RD)


strHost = "120.24.6.46"
HOST = strHost  # socket.inet_pton(socket.AF_INET,strHost)
PORT = 80

httpheader = '''
HTTP/1.1 200 OK
Context-Type: text/html
Server: Python-slp version 1.0
Context-Length: '''

lisfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lisfd.bind((HOST, PORT))
lisfd.listen(2)

signal.signal(signal.SIGINT, sigIntHander)

runflag = True
while runflag:
    try:
        confd, addr = lisfd.accept()
    except socket.error as e:
        if e.errno == errno.EINTR:
            print('get a except EINTR')
        else:
            raise
        continue

    if runflag == False:
        break;

    print( "connect by ", addr)
    data = confd.recv(1024)
    if not data:
        break
    print(data)
    confd.send(HttpResponse(httpheader, data))
    confd.close()
else:
    print('runflag#', runflag)

print('Done')