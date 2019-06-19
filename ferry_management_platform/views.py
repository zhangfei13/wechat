#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import requests
import urllib3
import urllib.request
import configparser
import json
import os
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import (TextMessage, VoiceMessage, ImageMessage, VideoMessage, LinkMessage, LocationMessage, EventMessage, ShortVideoMessage)

access_token = ""

currentDir, filename = os.path.split(os.path.abspath(__file__))
currentDir = currentDir.replace("\\", "/")
if currentDir.endswith('/') is False:
    currentDir = currentDir + '/'
config_file = currentDir + "../conf/config.ini"
url_base = ""
token = ""
appid = ""
appsecret = ""
encrypt_mode = ""
encoding_aes_key = ""
if os.path.exists(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    if config.has_option("SERVICE", "url"):
        url_base = config.get("SERVICE", "url")
    if config.has_option("WECHAT", "token"):
        token = config.get("WECHAT", "token")
    if config.has_option("WECHAT", "appid"):
        appid = config.get("WECHAT", "appid")
    if config.has_option("WECHAT", "appsecret"):
        appsecret = config.get("WECHAT", "appsecret")
    if config.has_option("WECHAT", "encrypt_mode"):
        encrypt_mode = config.get("WECHAT", "encrypt_mode")
    if config.has_option("WECHAT", "encoding_aes_key"):
        encoding_aes_key = config.get("WECHAT", "encoding_aes_key")

config = WechatConf(
        token=token,
        appid=appid,
        appsecret=appsecret,
        encrypt_mode=encrypt_mode,
        encoding_aes_key=encoding_aes_key
)
print("*********************************************", url_base, token, appid, appsecret, encrypt_mode, encoding_aes_key)

@csrf_exempt
def wechat_home(request):
    global url_base
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    wechat_instance = WechatBasic(conf=config)
    if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
        return HttpResponseBadRequest('Verify Failed')
    else:
        if request.method == 'GET':
            response = request.GET.get('echostr', 'error')
        else:
            try:
                wechat_instance.parse_data(request.body)
                message = wechat_instance.get_message()
                if isinstance(message, TextMessage):
                    reply_text = '''★想要知道你缴纳了多多少笔违法，点击<a href="%s/jilu/">这里</a>立刻查看缴款历史记录''' % url_base
                elif isinstance(message, VoiceMessage):
                    reply_text = 'voice'
                elif isinstance(message, ImageMessage):
                    reply_text = 'image'
                elif isinstance(message, LinkMessage):
                    reply_text = 'link'
                elif isinstance(message, LocationMessage):
                    reply_text = 'location'
                elif isinstance(message, VideoMessage):
                    reply_text = 'video'
                elif isinstance(message, ShortVideoMessage):
                    reply_text = 'shortvideo'
                else:
                    reply_text = '''感谢关注武汉交警！
★立刻加入V用户，不仅可以在线处理交通违法、还能享受学习减免3分、首违警告等福利哦！
很简单，点击下方菜单——警民互动——实名认证即可哒~

★回复【记录】查看本人在武汉交警微信上的缴款历史记录，看快去看看哦！'''
                response = wechat_instance.response_text(content=reply_text)
            except ParseError:
                return HttpResponseBadRequest('Invalid XML Data')
        return HttpResponse(response, content_type="application/xml")


def token():
    global access_token
    global config
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (config.appid, config.appsecret)
    result = requests.get(url, stream=True).content
    access_token = json.loads(result).get('access_token')
    print('access_token===%s' % access_token)
    return True


def createMenu():
    global access_token
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % access_token

    menu = {
        "button": [
            {
                "type": "view",
                "name": "V用户",
                "key": "button_0_0",
                "url": "%s/v_user/" % url_base,
                "sub_button": []
            },
            {
                "type": "view",
                "name": "惠民服务",
                "key": "button_1_0",
                "url": "%s/huimin_service/" % url_base,
                "sub_button": []
            },
            {
                "name": "警民互动",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "实名认证",
                        "key": "button_2_0",
                        "url": "%s/certification/" % url_base
                    },
                    {
                        "type": "view",
                        "name": "信息查询",
                        "key": "button_2_1",
                        "url": "%s/information_search/" % url_base
                    },
                    {
                        "type": "view",
                        "name": "交管12123",
                        "key": "button_2_2",
                        "url": "%s/jiaoguan12123/" % url_base
                    },
                    {
                        "type": "view",
                        "name": "我是好司机",
                        "key": "button_2_3",
                        "url": "%s/woshihaosiji/" % url_base
                    }
                ]
            }]
    }
    jsonStr = json.dumps(menu, ensure_ascii=False).encode('utf-8')

    http = urllib3.PoolManager()
    response = http.request("POST",
                            url,
                            headers={'Content-Type': 'application/json'},
                            body=jsonStr)
    resp_data = str(response.data, encoding="utf-8")
    print("注册menu:", resp_data)

def jilu(request):
    info_list = {}
    info_list['title'] = "违法记录"
    return render(request, 'jilu.html', {'info_list': info_list})

def v_user(request):
    info_list = {}
    info_list['title'] = "V用户"
    return render(request, 'v_user.html', {'info_list': info_list})


def huimin_service(request):
    info_list = {}
    info_list['title'] = "惠民服务"
    return render(request, 'huimin_service.html', {'info_list': info_list})


def certification(request):
    info_list = {}
    info_list['title'] = "实名认证"
    return render(request, 'certification.html', {'info_list': info_list})

def certification_inputinfo(request):
    info_list = {}
    info_list['title'] = "认证信息填写"
    return render(request, 'certification_inputinfo.html', {'info_list': info_list})

def information_search(request):
    info_list = {}
    info_list['title'] = "信息查询"
    return render(request, 'information_search.html', {'info_list': info_list})

def jiaoguan12123(request):
    info_list = {}
    info_list['title'] = "交管12123"
    return render(request, 'jiaoguan12123.html', {'info_list': info_list})

def woshihaosiji(request):
    info_list = {}
    info_list['title'] = "我是好司机"
    return render(request, 'woshihaosiji.html', {'info_list': info_list})

token()
createMenu()
