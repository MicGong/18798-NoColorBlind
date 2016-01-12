#!/usr/bin/python
from PIL import ImageTk, Image
import Tkinter as TK
import tkFont

from IshiTestPage import IshiTestPage

        


# class Anomolascope(TK.Frame):


def main():
    root = TK.Tk()
    ishiTestPage = IshiTestPage(root)
    root.configure(background = 'grey')
    root.geometry('{}x{}'.format(1000, 700))
    # root.attributes('-fullscreen', True)
    root.mainloop()

if __name__ == '__main__':
    main()

