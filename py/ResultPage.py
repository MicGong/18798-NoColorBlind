
from PIL import ImageTk, Image
import Tkinter as TK
import tkFont

import numpy as np
import cv2



class ResultPage(TK.Frame):
    def __init__(self, parent):
        # self.parent = TK.Toplevel(parent)
        TK.Frame.__init__(self, parent)
        self.parent = parent
        self.cap = cv2.VideoCapture(0)
        self.initUI()
        # self.showCamera()

    def initUI(self):
        self.parent.title('NoColorBlind')
        customFont1 = tkFont.Font(family = 'Helvetica', size = 40, weight = 'bold')
        customFont2 = tkFont.Font(family = 'Purisa', size = 25, weight = 'bold')

        self.titleLabel = TK.Frame(self.parent)
        self.titleLabel.pack(side = TK.TOP)
        self.titleLabel.label = TK.Label(self.titleLabel, width = 160, pady = 20,\
            text = 'No Color Blind ', font = customFont1, fg = 'red', bg = 'grey')
        self.titleLabel.label.pack(expand = 'no')

        self.imageLabel = TK.Frame(self.parent)
        self.imageLabel.pack(side = TK.TOP)
        self.imageLabel.label = TK.Label(self.imageLabel)
        self.imageLabel.label.pack()

    def showCamera(self):
        _, self.frame = self.cap.read()
        # self.frame = cv2.flip(self.frame, 1)
        self.cvtFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
        self.imgTk = ImageTk.PhotoImage(Image.fromarray(self.cvtFrame))
        self.imageLabel.label.image = self.imgTk
        self.imageLabel.label.configure(image = self.imgTk)
        self.imageLabel.label.after(50, self.showCamera)


def btnClicked(root):
    top = TK.Toplevel(root)
    anomTestPage = ResultPage(top)
    anomTestPage.showCamera()
    

root = TK.Tk()
# root.geometry('{}x{}'.format(1000, 700))

button = TK.Button(root, text = 'Result Window', command = lambda: btnClicked(root))
button.pack()

root.mainloop()