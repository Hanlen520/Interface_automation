# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Interface_automation
# author: "Lei Yong" 
# creation time: 2017/12/13 0013 22:33
# Email: leiyong711@163.com
import ConfigParser
import os
import time

config = ConfigParser.ConfigParser()


def w(name, passWord):
    if config.read('test.ini') == ['test.ini']:
        config.set('loginInfo','name',name)
        config.set('loginInfo', 'passWord', passWord)
        config.write(open('test.ini', 'wb'))
    else:
        config.add_section('loginInfo')
        config.set('loginInfo','name',name)
        config.set('loginInfo','passWord',passWord)
        config.write(open('test.ini','wb'))

k = []
def r():
    try:
        config.read('test.ini')
        k.append(config.get('loginInfo', 'name'))
        k.append(config.get('loginInfo', 'passWord'))
        return k
    except:
        return ''
