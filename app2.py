#s24001
#app2.py

import tkinter as tk #tkinterをimportしてtkと略して扱う

def dispLabel():
    lbl.config(text="こんにちは")

root =tk.Tk() #画面を作る
root.geometry("400x200") #画面の大きさを決める

lbl = tk.Label(text="LABEL", font=("Helvetica", 20)) #ラベルを作る
btn = tk.Button(text="PUSH", command=dispLabel, font=("Helvetica", 20)) #ボタンを作る

lbl.pack() #画面にラベルを配置する
btn.pack() #画面にボタンを配置する
tk.mainloop() #作ったウィンドウを表示する
