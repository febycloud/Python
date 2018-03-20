#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import Tkinter
import instaLooter

root = Tkinter.Tk()
root.title(u"InstaDownloader")
root.geometry("300x300")

#ラベル
Static1 = Tkinter.Label(text=u'this is made in china')
Static1.pack()

#エントリー
EditBox = Tkinter.Entry(width=30)
EditBox.insert(Tkinter.END,"input instagram ID")
EditBox.pack()
EditBox.place(x=40, y=30)
instaID = EditBox.get()

#instadownload
def instaDownload(event):
    instaLooter instaID ./instaID

#ボタン
Button = Tkinter.Button(text=u'Download')
Button.place(x=105, y=70)
Button.bind("<Button-1>",instaDownload) 

root.mainloop()
