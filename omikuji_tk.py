# s24001
# おみくじプログラムGUIアプリ

import tkinter as tk

root = tk.Tk()

root.geometry("800x600")
root.title("おみくじ")
import random
lbl = tk.Label(text="大吉","中吉","小吉","凶")
lbl.pack(random.choice())


root.mainloop()
