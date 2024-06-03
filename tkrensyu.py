# GUIで動くアプリを作ってみるよ

import tkinter as tk 

root = tk.Tk() #初めのおまじない

root.geometry("600x400") #ウィンドウのサイズを決める
root.title("ハローアプリ") #ウィンドウのタイトルを決める
lbl = tk.Label(text="こんにちは世界") #いつもの
lbl.pack() #lblを配置する
lbl = tk.Label(text="はじめてのGUIアプリ")
lbl.pack()




root.mainloop() 
