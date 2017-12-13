# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Interface_automation
# author: "Lei Yong" 
# creation time: 2017/12/13 0013 22:34
# Email: leiyong711@163.com
import webbrowser
import time
import os
import Tkinter
from Tkinter import *
import ttk
import juanzeng
import urllib
import json
import gui
import tkMessageBox
from PIL import Image, ImageTk
from loginInfo import *

url2 = 'https://orangep.cn:9999/login'
version = '1.4'
banben = u'\n\n当前版本 %s' % version


# 初始化
List_Content = []
box_1 = True


def login():
    root = Tkinter.Tk()
    root.iconbitmap('img\\logo2.ico')
    root.title('接口功能自动化 登录 (Last indulge)')
    root.geometry('360x220+570+320')
    root.resizable(False, False)
    canvas = Tkinter.Canvas(root, width=1920, height=1080, bg='#EAEAEA')
    image1 = ImageTk.PhotoImage(file="img\\bz3.jpg")
    canvas.create_image(0, 200, image=image1)

    # 在大窗口下定义一个顶级菜单实例
    menubar = Menu(root)

    def xp():
        tkMessageBox.askyesno('帮助', '如发现BUG请通过邮件\nleiyong711@163.com\n联系作者。\n\n\n     当前版本 %s'
                              % version)

    def jz():
        juanzeng.jz1()

    menubar.add_command(label='帮助', command=xp)
    menubar.add_command(label='赞助', command=jz)

    def cgpawd():
        url = 'https://orangep.cn:9999/cgpawd'
        webbrowser.open(url, new=0, autoraise=True)

    def re():
        url = 'https://orangep.cn:9999/register'
        webbrowser.open(url, new=0, autoraise=True)

    def click_c1():
        global box_1
        box_1 = not box_1

    def ks1():
        na = name_win.get()
        pa = password_win.get()
        if na == '':
            tkMessageBox.showerror('警告', '请填写账号')
        elif pa == '':
            tkMessageBox.showerror('警告', '请填写密码')
        else:
            if box_1 == True:
                w(na.encode('GB2312'), pa.encode('GB2312'))
            else:
                w('', '')
            na1 = na.encode('GB2312')
            pa1 = pa.encode('GB2312')

            # root.quit()
            # try:
            data = {"name": na1, "password": pa1, "Program_name": "Interface_function_test", "version": version}
            date = urllib.urlencode(data)
            try:
                html = urllib.urlopen(url2, date).read()
                print html
                html1 = json.loads(html)
                loginrt = html1
                print 'info：%s' % loginrt
            except:
                print 'error：server解析失败'
                loginrt = '服务器错误'

            k = 0
            b = loginrt
            try:
                if b == '服务器错误':
                    k = 9
                    # gui.sj('异常', '连接服务器异常\r\n\n解决方法：\r\n  '
                    #              '1.请查看当前网络是否正常\n  '
                    #              '2.此应用是否被360类软件禁网\n  '
                    #              '3.如若无法解决请通过邮件联系作者\n  leiyong711@163.com')
                    tkMessageBox.showinfo('异常', '连接服务器异常\r\n\n解决方法：\r\n  '
                                          '1.请查看当前网络是否正常\n  '
                                          '2.此应用是否被360类软件禁网\n  '
                                          '3.如若无法解决请通过邮件联系作者\n  leiyong711@163.com')

                elif b['state'].encode('utf-8') == '正常':
                    try:
                        tkMessageBox.showinfo(b['version']['win'], b['version']['info'])
                        root.destroy()
                        gui.lei(version)

                    except:
                        root.destroy()
                        gui.lei(version)

                elif b['state'].encode('utf-8') == '版本过期':
                    tkMessageBox.showerror(b['error']['win'], b['error']['info'] + banben)
                    root.destroy()

                elif k == 0:
                    tkMessageBox.showerror(b['error']['win'], b['error']['info'] + banben)


            except:
                if k == 0:
                    tkMessageBox.showerror(b['error']['win'], b['error']['info'] + banben)

    # 配置
    # name = Tkinter.Label(root, text='用户名：', bg='#EAEAEA')
    # password = Tkinter.Label(root, text='密码：', bg='#EAEAEA')
    canvas.create_text(50, 60, text='用户名：')
    canvas.create_text(50, 90, text='密码：')
    canvas.create_text(135, 125, text='记住信息')

    canvas.create_text(300, 175, text='版本 %s' % version, fill='#00B2EE', font=("黑体", 12, "bold"))
    name_win = Tkinter.Entry(root, width=30)  # Mokey测试‘随机种子数量’输入框
    password_win = Tkinter.Entry(root, width=27)  # Mokey测试‘随机种子数量’输入框

    password_win['show'] = '*'
    info = r()
    if info != '':
        name_win.insert(0, info[0])
        if info[1] != '':
            password_win.insert(0, info[1])

    login = Tkinter.Button(root, text='登录', bg='#B8B8B8', font=('', 11), command=ks1)
    rel = Tkinter.Button(root, text='注册', bg='#B8B8B8', font=('', 11), command=re)

    def on_off():
        print btonoff['image']
        if btonoff['image'] == 'pyimage2':
            btonoff['image'] = k1
        else:
            btonoff['image'] = k
        if btonoff['image'] == 'pyimage2':
            password_win['show']= ''
        else:
            password_win['show']='*'

    def imag(path, w_box=31, h_box=18):

        def resize(w, h, w_box, h_box, pil_image):
            '''
            对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
            '''
            f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
            f2 = 1.0 * h_box / h
            factor = min([f1, f2])
            width = int(w * factor)
            height = int(h * factor)
            return pil_image.resize((width, height), Image.ANTIALIAS)

        # 以一个PIL图像对象打开
        pil_image = Image.open(path)
        # 获取图像的原始大小
        w, h = pil_image.size
        # 缩放图像让它保持比例，同时限制在一个矩形框范围内
        pil_image_resized = resize(w, h, w_box, h_box, pil_image)
        return ImageTk.PhotoImage(pil_image_resized)

    k = imag("img\\jz.png")
    k1 = imag('img\\jz1.png')
    k2 = imag('img\\butt.png', 70, 70)

    ck1 = Checkbutton(root, bd=0, command=click_c1, relief=FLAT)
    ck1.select()
    btonoff = Tkinter.Button(root, image=k1, bd=-50, text="on", command=on_off)
    btonoff1 = Tkinter.Button(root, image=k2, bd=-50, text="忘记密码？", command=cgpawd, relief=FLAT)

    # 布局
    # canvas.create_window(50, 60, window=name)  # 品牌文字布局
    # canvas.create_window(50, 90, window=password)  # 品牌文字布局
    canvas.create_window(190, 60, window=name_win)  # 品牌文字布局
    canvas.create_window(178, 90, window=password_win)  # 品牌文字布局
    canvas.create_window(130, 160, window=login)  # 品牌文字布局
    canvas.create_window(210, 160, window=rel)  # 品牌文字布局
    canvas.create_window(95, 125, window=ck1)
    canvas.create_window(260, 125, window=btonoff1)
    canvas.create_window(285, 91, window=btonoff)

    canvas.pack()
    root['menu'] = menubar
    root.mainloop()


login()
