import tkinter as tk
import random as rand
from PIL import Image as img
from PIL import ImageTk as imgtk
from pathlib import Path as path

dir = "data"
col_len = 4
thumb_width = 50

# メインクラス
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.tile()

    # 画像を配列で読み込み、シャッフルし、それぞれリサイズし、全てをgridで表示する
    def tile(self):
        self.resized_pics = []
        self.path = list(path(dir).iterdir())
        rand.shuffle(self.path)
        for i in range(len(self.path)):
            self.raw_pic = img.open(self.path[i])
            self.resized_pics.append(self.raw_pic.resize((thumb_width, int(thumb_width * self.raw_pic.height / self.raw_pic.width))))
            self.resized_pics[i] = imgtk.PhotoImage(self.resized_pics[i])
            self.label = tk.Label(image=self.resized_pics[i], bd=0)
            self.label.grid(column=i % col_len, row=int(i / col_len), sticky=tk.S)


# メイン処理
root = tk.Tk()
root.title("test")

app = App(master=root)

app.mainloop()
