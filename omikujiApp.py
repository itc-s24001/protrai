# s24001
# おみくじアプリプログラム

import tkinter as tk
import random

def dispLabel():
    kuji = ["大吉","中吉","小吉","凶","大凶","半吉","末吉","大大吉"]
    lbl.config(text=random.choice(kuji))

root =tk.Tk() #画面を作る
root.geometry("400x200") #画面の大きさを決める

lbl = tk.Label(text="おみくじ", font=("Helvetica", 20)) #ラベルを作る
btn = tk.Button(text="PUSH", command=dispLabel, font=("Helvetica", 20)) #ボタンを作る

lbl.pack() #画面にラベルを配置する
btn.pack() #画面にボタンを配置する
tk.mainloop() #作ったウィンドウを表示する

