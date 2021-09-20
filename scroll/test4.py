import tkinter as tk
import tkinter.scrolledtext as tks
import random as rand
from PIL import Image as img
from PIL import ImageTk as imgtk
from pathlib import Path as path

dir = "data"
thumb_width = 200


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.tile()

    def tile(self):
        self.stxt = tks.ScrolledText(state=tk.DISABLED, cursor="arrow")
        self.stxt.pack(fill=tk.BOTH, expand=True)
        self.resized_pics = []
        self.path = list(path(dir).iterdir())
        rand.shuffle(self.path)
        for i in range(len(self.path)):
            self.raw_pic = img.open(self.path[i])
            self.resized_pics.append(self.raw_pic.resize(self.getSize(self.raw_pic),resample=img.BOX))
            self.resized_pics[i] = imgtk.PhotoImage(self.resized_pics[i])
            self.imageLabel(self.stxt, self.resized_pics[i])

    def imageLabel(self, stxt, image):
        self.frame = tk.Frame(stxt, width=thumb_width, height=self.getSize(self.raw_pic)[1])
        self.label = tk.Label(self.frame, image=image, bd=0)
        self.label.pack()
        stxt.window_create(tk.END, align=tk.BASELINE, window=self.frame)

    def getSize(self, image):
        return (thumb_width, int(thumb_width * self.raw_pic.height / self.raw_pic.width))


# メイン処理
root = tk.Tk()
root.title("test")

app = App(master=root)

app.mainloop()
