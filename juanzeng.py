# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Interface_automation
# author: "Lei Yong" 
# creation time: 2017/12/13 0013 22:32
# Email: leiyong711@163.com
import Tkinter
from PIL import Image, ImageTk

def jz1():
    # root1 = Tkinter.Tk()
    root = Tkinter.Toplevel()

    root.iconbitmap('img\\logo2.ico')
    root.title('赞助')
    root.geometry('420x380+750+300')
    root.resizable(False, False)
    canvas = Tkinter.Canvas(root,width=600, height=400, bg='blue')
    image = ImageTk.PhotoImage(file="img\\bz6.jpg")
    canvas.create_image(300, 50, image=image)
    canvas.create_text(200, 25, text='如果帮助到您，可为服务器', fill='#87CEFF', font=("黑体", 14))
    canvas.create_text(200, 50, text='贡献一份力量', fill='#EE7600', font=("黑体", 16, "bold"))
    zhifb_Photo = ImageTk.PhotoImage(file='img\\gr.png')
    zhifubao = Tkinter.Label(root, imag=zhifb_Photo)
    canvas.create_window(210, 210, window=zhifubao)
    # canvas.create_image(0, 0, image=image, anchor=NW)
    # canvas.pack(expand=YES, fill=BOTH)
    canvas.pack()
    root.mainloop()

if __name__ == '__main__':
    jz1()


