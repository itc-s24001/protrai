#s24001
#画像に色んな処理をする

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).convert("L") \
               .rotate(90).transpose(PIL.Image.FLIP_LEFT_RIGHT) \
               .resize((32, 32)).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData
    lbl2 = tk.Label(text=path, font=("Helvetica", 20))
    lbl2.pack()

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)

root = tk.Tk()
root.geometry("600x550")

lbl = tk.Label(text="画像表示アプリバージョン2.0", font=("Helvetica", 20))
btn = tk.Button(text="ファイルを開く", command=openFile)
imageLabel = tk.Label()
lbl.pack()
btn.pack()
imageLabel.pack()

tk.mainloop()
