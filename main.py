# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Interface_automation
# author: "Lei Yong" 
# creation time: 2017/12/13 0013 22:33
# Email: leiyong711@163.com
import re
import sys
import urllib     # 把这两个库导入
import urllib2

from excel_r import excel_r

reload(sys)
sys.setdefaultencoding('utf-8')


def POST(url, data):
    data_code = urllib.urlencode(data)  # 把参数进行编码
    # print url,data_code
    # url2 = urllib2.Request(url,data1)  # 用.Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
    response = urllib2.urlopen(url,data_code)  # 用.urlopen打开上一步返回的结果，得到请求后的响应内容
    # print response
    apicontent = response.read()  # 将响应内容用read()读取出来
    return apicontent
    # json.loads(apicontent)['code']


def GET(url, api):
    url = url + '?' + api
    req = urllib2.Request(url)
    # print req
    res_data = urllib2.urlopen(req)
    # print res_data
    res = res_data.read()
    return res


def ks(fname):
    asp, info = excel_r(fname)
    for i in range(1, len(asp)):
        request_type = asp[i][4].upper()
        if request_type == 'POST':
            l = []
            data = {}
            jiequ = asp[i][3].split(',')
            for k in range(len(jiequ)):
                spli = jiequ[k].split('=')
                l.append([])
                for j in range(len(spli)):
                    l[k].append(spli[j])
                data.setdefault(l[k][0], l[k][1])
            returned_value = POST(asp[i][2], data)
            # fanhui = cmp(returned_value, asp[i][5])
            fanhui = re.search(asp[i][5], returned_value)
            # print fanhui
            if fanhui != None:
                asp[i][6] = returned_value
                asp[i][7] = 'Pass'
                spc = asp
            # elif fanhui == -1:
            #     asp[i][6] = returned_value
            #     asp[i][7] = 'Fail'
            #     spc = asp

            else:
                asp[i][6] = returned_value
                asp[i][7] = 'Fail'
                spc = asp

        elif request_type == 'GET':
            data = asp[i][3].replace(',', '&')
            # print asp[i][2], data
            returned_value = GET(asp[i][2], data)
            # fanhui = cmp(returned_value, asp[i][5])
            fanhui = re.search(asp[i][5], returned_value)
            # print fanhui
            if fanhui != None:
                asp[i][6] = returned_value
                asp[i][7] = 'Pass'
                spc = asp
            # elif fanhui == -1:
            #     asp[i][6] = returned_value
            #     asp[i][7] = 'Fail'
            #     spc = asp

            else:
                asp[i][6] = returned_value
                asp[i][7] = 'Fail'
                spc = asp

        else:
            asp[i][6] = u'请求类型错误'
            asp[i][7] = 'error'
            spc = asp

    return spc,info


