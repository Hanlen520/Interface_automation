# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Interface_automation
# author: "Lei Yong" 
# creation time: 2017/12/13 0013 22:31
# Email: leiyong711@163.com
import os
import time

# from pyExcelerator import *
import xlwt
from main import ks




def exceslw(yong, fname):
    def style(name,height,bold,s,color=1,):
        u'字体，高度，背景色'
        pattern = xlwt.Pattern()  # 创建模式
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern.pattern_fore_colour = color  # "可能是:8到63。0 =黑,1 =白,2 =红,3 =绿色,4 =蓝色,5 =黄色,6 =品红色,
        # 7 =青色,16 =栗色,17 =深绿色,18 =深蓝色,19 =深黄色,几乎布朗),20 =暗紫红色,21 =水鸭,22 =浅灰色,23 =深灰色,不胜枚举…"
        style = xlwt.XFStyle()  # Create the Pattern

        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 'Times New Roman'
        font.bold = bold
        font.color_index = 4
        font.height = height
        font.colour_index = s  # 设置其字体颜色
        style.font = font


        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
        alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
        style.alignment = alignment

        style.pattern = pattern  # Add Pattern to Style
        return style

    def style1():
        pattern = xlwt.Pattern()  # 创建模式
        style = xlwt.XFStyle()  # Create the Pattern
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
        alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
        style.alignment = alignment

        style.pattern = pattern  # Add Pattern to Style
        return style

    aps = [u'用例ID', u'用例名', u'url', u'参数值', u'请求方式', u'期望', u'实际返回', u'结果']
    # print aps
    w = xlwt.Workbook()  #创建一个工作簿
    ws = w.add_sheet('Sheet1')  #创建一个工作表
    pc, info = ks(yong)
    # print pc

    ws.write_merge(0, 0, 0, 7, u'接口功能测试报告', style(u'宋体', 360, True,0x01,4))
    for i in range(len(pc)):
        for j in range(len(pc[i])):
        #     ws.write(i,j,aps[j]) #在1行1列写入bit
            a = pc[i][j]
            if j == 6:
                ws.write(i+1, j, a.decode('utf-8'))  # 在1行1列写入bit
            else:
                # if j == 7 and a == 'Fail':
                #     ws.write(i, j, a, style(2))
                # elif j == 7 and a == 'Pass':
                #     ws.write(i, j, a, style(3))
                if j == 7 and a == 'Fail':
                    ws.write(i+1, j, a, style(u'宋体', 360, False,0x01,2))
                elif j == 7 and a == 'Pass':
                    ws.write(i+1, j, a, style(u'宋体', 360, False,0x01,3))
                else:
                    try:
                        ws.write(i+1, j, a.decode('utf-8'), style1())
                    except:
                        ws.write(i+1, j, a, style1())

                # elif :
                #     ws.write(i, j, a)
    timestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    ws.write(len(pc) + 2, 0, u'测试时间：%s' % timestr)
    w.save('%s\\case_result.xlsx'% fname)  #保存
    return pc,info

def exceslws(path):
    pc = [[u'用例ID', u'用例名', u'url', u'参数值', u'请求方式', u'期望', u'实际返回', u'结果'], [1.0, u'图灵api接口GET请求', u'http://www.tuling123.com/openapi/api', u'key=305122eaa84142aa8b076a962ca87523,info=笑话', u'GET', u'text', '', ''], [2.0, u'图灵api接口get请求', u'http://www.tuling123.com/openapi/api', u'key=305122eaa84142aa8b076a962ca87523,info=笑话', u'POST', u'"code":60000', '', ''],
          [3.0, u'图灵api接口get请求', u'http://www.tuling123.com/openapi/api',
           u"多个参数用,号分割", u'Get', u'"code":60000', u'使用时请删除此三条例程用例', '']]
    # print aps
    w = xlwt.Workbook()  #创建一个工作簿
    ws = w.add_sheet('Sheet1')  #创建一个工作表
    # ws = copy('..\\Case\\test.xlsx')

    # print pc
    for i in range(len(pc)):
        for j in range(len(pc[i])):
        #     ws.write(i,j,aps[j]) #在1行1列写入bit
            a = pc[i][j]
            if j == 6:
                ws.write(i, j, a)  # 在1行1列写入bit
            else:
                ws.write(i, j, a)

    a = os.path.exists('%s' % path)
    if a == False:
        os.makedirs('%s' % path)
    w.save('%s\\case.xlsx' % path)  #保存
    return pc

# if __name__ == '__main__':
#     a = apc()
#     a.exceslws(r'I:\code\report')
