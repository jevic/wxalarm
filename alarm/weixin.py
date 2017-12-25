#!/usr/bin/python
# coding: utf-8
# Auth: jieyang <jieyang@gmail.com>
#
from urllib import quote
import urllib
import urllib2
import json
import sys
import requests
from os.path import sep, getsize

class WeixinAlarm():
    def __init__(self,corpid,secret):
        self.corpid = corpid
        self.secret = secret
        self.gettoken = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (self.corpid,self.secret)
        self.Sends = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="

    @property
    def token(self):
        '''获取token'''
        try:
            req = urllib2.Request(self.gettoken)
            response = urllib2.urlopen(req,timeout=20)
            Datas = response.read()
            codes = json.loads(Datas)
            TOKEN = codes.get('access_token')
            return TOKEN
        except Exception,e:
            return e2

    @property
    def SendURL(self):
        return self.Sends + self.token

    def SendText(self,agentid,content):
        ''' 发送文本信息 '''
        Bodys = {
        "touser" : "@all",
        "msgtype": "text",
        "agentid": agentid,
        "text": {
        "content": "%s" % content
        },
        "safe": 0
        }
        try:
            req = urllib2.Request(self.SendURL)
            req.add_header('Content-Type', 'application/json')
            response = urllib2.urlopen(req,json.dumps(Bodys))
            print response.read()
        except Exception,e:
            return e

    def SendMedia(self,agentid,media_id,mtype):
        ''' 发送文件 '''
        msgtype = "image"
        if mtype <> 1:
            msgtype = "file"
        Bodys = {
        "touser" : "@all",
        "msgtype": "%s" % (msgtype),
        "agentid": agentid,
        "%s" % msgtype: {
        "media_id": "%s" % media_id
        },
        "safe": 0
        }
        try:
            req = urllib2.Request(self.SendURL)
            req.add_header('Content-Type', 'application/json')
            response = urllib2.urlopen(req,json.dumps(Bodys))
            print response.read()
        except Exception,e:
            return e

    def upload(self,myfile):
        f = open(myfile,'rb')
        ftype = f.name.split('.')[-1].lower()
        msgtype = 1
        if ftype == 'jpg' or ftype == 'png':
            _UploadURL = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=image" % self.token
        else:
            _UploadURL = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=file" % self.token
            msgtype = 2
        try:
            files = {'file': (f.name.split(sep)[-1],f)}
            r = requests.post(_UploadURL,files=files)
            f.close
        except Exception,e:
            print e
        if 'media_id' in r.json():
            media_id =  r.json()['media_id']
        else:
            return 'errcode: %s, errmsg: %s' % (r.json()['errcode'],r.json()['errmsg'])
        return media_id,msgtype

