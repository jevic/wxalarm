#!/usr/bin/python
# coding: utf-8
# Auth: jieyang <jieyang@gmail.com>
# Version: 2.0
#
import os
from werkzeug import secure_filename
from weixin import WeixinAlarm
from flask import Flask,request,render_template,redirect,url_for


Corpid=
Secret=
agentid=

alarm = WeixinAlarm(Corpid,Secret)
app = Flask(__name__)

@app.route('/send_message',methods=['GET','POST'])
def Send():
    try:
        content = request.args.get('content')
        if content:
            alarm.SendText(agentid,content)
            return "sendMessage OK"
        else:
            return "sendMessage Error"
    except Exception,e:
        return e

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=51001)
