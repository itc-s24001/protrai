#s24001
#時間を表示させる「時計アプリ」を作る

import datetime
import tkinter as tk #GUIでアプリを作れるモジュール

#時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    lbl.config(text=current_time)
    root.after(1000, update_time) #自分をもう一度呼ぶ。()を入れない

#tkinterのウィンドウを作成
root = tk.Tk() #初め

root.title("現在の時刻")

lbl = tk.Label()
lbl.config(text="", font=("Helvetica", 20)) #自由にフォントやサイズ変更可能
lbl.pack()

#関数の呼び出し
update_time()

root.mainloop() #終わり
