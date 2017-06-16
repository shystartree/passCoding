#!/usr/bin/env python
# coding=utf-8
from Tkinter import *
import ttk
import decode
import encode

root = Tk()
root.title('00 coding')
root.geometry('600x400')

def hello():
    print('hello')

def about():
    fAbout=open('about.txt','w')

#创建菜单
menubar = Menu(root)

# 创建下拉菜单File，然后将其加入到顶级的菜单栏中
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# 创建另一个下拉菜单Edit
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)
# 创建下拉菜单Help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# 显示菜单
root.config(menu=menubar)

frm = Frame(root,).pack()  #主框架

#顶部框架
frmTop=Frame(frm,width=600,height=100,)

frmTopLeft=Frame(frmTop)
Label(frmTopLeft,).pack(side=LEFT)
Label(frmTopLeft,text='coding method',width=20,height=4,).pack(side=LEFT)
codingMethod=StringVar()
Entry(frmTopLeft,textvariable=codingMethod,width=12,).pack(side=RIGHT)
coText=codingMethod.get()     #coding method var

frmTopLeft.pack(side=LEFT)

frmTopRight=Frame(frmTop)
Label(frmTopRight,text='or',width='10',).pack(side=LEFT)
codingMethod=StringVar(frmTopRight)
codingMethodChosen=ttk.Combobox(frmTopRight,width=10,textvariable=codingMethod,values=['null','1','2','3'])
codingMethodChosen.current(0)
Label(frmTop,width=8,).pack(side=RIGHT)
codingMethodChosen.pack(side=RIGHT)
frmTopRight.pack(side=RIGHT)

frmTop.pack(side=TOP)

frmB=Frame(root,width=200,height=100,)

#左边框架
frmLeft=Frame(frmB)
messageTextLeft=Text(frmLeft,width=35,height=23)
messageTextLeft.insert(1.0,'plaintxt')
messageTextLeft.pack()
frmLeft.pack(side=LEFT)

#右边框架
frmRight=Frame(frmB)
messageTextRight=Text(frmRight,width=35,height=23)
messageTextRight.insert(1.0,'pycipher')
messageTextRight.pack()
frmRight.pack(side=RIGHT)

#中间框架
frmMid=Frame(frmB,)
Label(frmMid,width='8',height='5',).pack()
Button(frmMid,text="加密",width='8',height='1',).pack()
Label(frmMid,text='--->',height=2).pack()
Button(frmMid,text="解密",width='8',height='1').pack()
Label(frmMid,text='<---',height=2).pack()
frmMid.pack()

frmB.pack()

#root.bind('<Return>',lambda event:print_content())

root.mainloop()