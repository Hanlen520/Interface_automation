# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Interface_automation
# author: "Lei Yong" 
# creation time: 2017/12/13 0013 22:31
# Email: leiyong711@163.com
import Tkinter
import datetime
import ttk
import tkMessageBox
import juanzeng
from Tkinter import *
from excel_w import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk

moPath = ''
yongli = ''
baog = ''


def lei(version):
    root = Tkinter.Tk()
    root.iconbitmap('img\\logo2.ico')
    root.title('接口测试小工具(Last indulge)')
    root.geometry('380x560+750+300')
    root.resizable(False, False)

    canvas = Tkinter.Canvas(root, width=1920, height=1080, bg='#EAEAEA')
    # image1 = ImageTk.PhotoImage(file="bz6.jpg")
    image1 = ImageTk.PhotoImage(file="img/hei.jpg")
    canvas.create_image(200, 400, image=image1)
    canvas.pack()

    # 在大窗口下定义一个顶级菜单实例
    menubar = Menu(root)

    def mobanP():
        global moPath
        fpath = askdirectory()
        if fpath != '':
            moPath = fpath
            path_input.insert(0, moPath)
            print fpath
        # TODO 模板导出路径选择

    def yongliP():
        global yongli
        fpath = filedialog.askopenfilename(filetypes=[("xlsx","*.xlsx"), ("xls","*.xls"),("all","*.*")])
        if fpath != '':
            yongli = fpath
            yong_input.insert(0, yongli)
            print fpath
        # TODO 用例导入路径选择

    def baoP():
        global baog
        fpath = askdirectory()
        if fpath != '':
            baog = fpath
            baogao_input.insert(0,baog)
            print fpath
        # TODO 报告导出路径选择

    def jz():
        juanzeng.jz1()

    def xp():
        tkMessageBox.askyesno('帮助', '如发现BUG请通过邮件\nleiyong711@163.com\n联系作者。\n\n\n     当前版本 %s'
                              % version)

    menubar.add_command(label='帮助', command=xp)
    menubar.add_command(label='赞助', command=jz)

    def daochupath():
        if moPath == '':
            tkMessageBox.showerror('警告', '请填写正确的模板导出路径')
        else:
            exceslws(moPath)
            pd = os.path.exists(moPath)
            print pd
            if pd == True:
                tkMessageBox.showinfo('导出用例模板', '用例模板成功导出\n\n请到 %s 查看case.xlsx' %moPath)
            else:
                tkMessageBox.showerror('导出用例模板', '用例模板导出失败')
            # TODO 导出测试用例模板

    def satrt():
        yong_path = yongli
        baogao_path = baog
        if yong_path == '':
            tkMessageBox.showerror('警告', '请填写正确的用例导入路径')
        elif baogao_path == '':
            tkMessageBox.showerror('警告', '请填写正确的测试报告导出路径')
        else:
            yong_pd = os.path.exists(yong_path)
            if yong_pd == False:
                tkMessageBox.showerror('用例导入', '用例导入失败\n\n请查看路径或用例名是否正确')
            start = datetime.datetime.now()
            print '接口测试开始'
            log_win.insert(0,'接口测试开始')
            k, info = exceslw(yong_path, baogao_path)
            log_win.insert(0, info)
            print '接口测试结束'
            log_win.insert(0, '接口测试结束')
            end = datetime.datetime.now()
            Time_consuming = str(end - start)[:-7]  # 用测试结束时间-开始时间得到测试耗时，再把时间转成字符串并去掉小数部分
            print '测试耗时：%s' % Time_consuming
            log_win.insert(0, '测试耗时：%s' % Time_consuming)

            baoga_pd = os.path.exists('%s\\case_result.xlsx'% baogao_path)
            if baoga_pd == True:
                tkMessageBox.showinfo('测试报告', '导出成功\n\n请查看测试报告\n %s\\case_result.xlsx'% baogao_path)
            else:
                tkMessageBox.showerror('测试报告', '导出失败请重试\n\n若重试多次失败请联系作者')

    # 文字配置
    canvas.create_text(180, 20, text='接口功能自动化', fill='#1C86EE', font=("黑体", 22, "bold"))
    canvas.create_text(60, 60, text='模板导出路径：')
    canvas.create_text(60, 130, text='用例导入路径：')
    canvas.create_text(60, 170, text='测试报告路径：')
    canvas.create_text(60, 330, text='测试信息：')
    canvas.create_text(180, 480, text='版本 %s' % version, fill='#00B2EE', font=("黑体", 12, "bold"))
    # canvas.create_text(160, 445, text='如果帮助到您，点击菜单栏', fill='#0000EE', font=("黑体", 14))
    # canvas.create_text(320, 445, text='赞助', fill='#CD6600', font=("黑体", 20, "bold"))
    # canvas.create_text(110, 480, text='可为服务器', fill='#0000EE', font=("黑体", 14))
    # canvas.create_text(250, 480, text='贡献一份力量', fill='#CD6600', font=("黑体", 20, "bold"))

    # 按钮配置
    mobanb = Tkinter.Button(root, text='导出模板', bg='#B8B8B8', font=('', 11), command=daochupath)
    satrta = Tkinter.Button(root, text='开始测试', bg='#B8B8B8', font=('', 11), command=satrt)
    mobanPath = Tkinter.Button(root, text='打开', bg='#B8B8B8', font=('', 10), command=mobanP)
    yongliPath = Tkinter.Button(root, text='打开', bg='#B8B8B8', font=('', 10), command=yongliP)
    baogaoPath = Tkinter.Button(root, text='打开', bg='#B8B8B8', font=('', 10), command=baoP)

    # 输出文本配置
    log_win = Tkinter.Listbox(root, width=30, height=10)  # 运行日志显示
    yong_input = Tkinter.Listbox(root, width=30, height=1)  # ‘导出测试用例’输入框
    path_input = Tkinter.Listbox(root, width=30, height=1)  # ‘导入测试用例路径’输入框
    baogao_input = Tkinter.Listbox(root, width=30, height=1)  # ‘测试报告’输出

    # 输出文本布局
    canvas.create_window(210, 330, window=log_win)  # ‘运行日志’文字布局
    canvas.create_window(210, 60, window=path_input)  # ‘用例模板导出’文字布局
    canvas.create_window(210, 130, window=yong_input)  # ‘测试用例导入路径’文字布局
    canvas.create_window(210, 170, window=baogao_input)  # ‘测试报告导出路径’文字布局

    # 按钮布局
    canvas.create_window(180, 95, window=mobanb)  # ‘导出模板’按钮布局
    canvas.create_window(180, 205, window=satrta)  # ‘开始测试’按钮布局
    canvas.create_window(340, 60, window=mobanPath)  # ‘模板路径’打开按钮布局
    canvas.create_window(340, 130, window=yongliPath)  # ‘用例导入’打开按钮布局
    canvas.create_window(340, 170, window=baogaoPath)  # ‘测试报告’打开按钮布局

    # 菜单实例应用到大窗口中
    root['menu'] = menubar
    root.mainloop()

def sj(win, info):
    root = Tkinter.Tk()
    root.iconbitmap('img\\logo.ico')
    root.title('测试小工具(Last indulge)')
    root.geometry('350x550')
    root.resizable(False, False)
    tkMessageBox.showinfo(win, info)


def error(win, info):
    root = Tkinter.Tk()
    root.iconbitmap('img\\logo.ico')
    root.title('测试小工具(Last indulge)')
    root.geometry('350x550')
    root.resizable(False, False)
    tkMessageBox.showerror(win, info)

if __name__ == '__main__':
    lei('1.4')

