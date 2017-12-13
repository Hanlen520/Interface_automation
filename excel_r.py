# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Interface_automation
# author: "Lei Yong" 
# creation time: 2017/12/13 0013 22:30
# Email: leiyong711@163.com
import xlrd


def excel_r(fname):
    # fname = "..\\Case\\case.xlsx"
    bk = xlrd.open_workbook(fname)
    try:
        sh = bk.sheet_by_name('Sheet1')
    except:
        print "%没有表名为Sheet1的" % fname
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    info = '用例行数：%s  用例列数：%s' % (nrows, ncols)
    a = []
    for i in range(0, nrows):
        c = sh.row_values(i)
        # if i == 0:
        #     continue
        # else:
        #     c[0] = int(c[0])
        #     c[6] = int(c[6])
        a.append(c)
    return a, info
#     print a
# if __name__ == "__main__":
#     a = excel()
#     print a[2]

