#s24001
#エントリーウィジェット税込み計算プログラム

import tkinter as tk

def dispLabel():
    a = int(entry.get())
    lbl.config(text=f"税込み価格は{a * 1.1}円です")


root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200")

lbl = tk.Label(text="金額を入力してください", font=("Helvetica", 20))
entry = tk.Entry(font=("Helvetica", 20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
