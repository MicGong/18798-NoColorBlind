

from PIL import ImageTk, Image
import Tkinter as TK
import tkFont
import tkMessageBox

import cv2

# from IshiTestPage import IshiTestPage
# from ResultPage import ResultPage
from ResultPageCV import ResultPageCV

def main():
    root = TK.Tk()
    anomTestPage = AnomTestPage(root)
    # root.configure(background = '#fff')
    root.geometry('{}x{}'.format(1000, 700))
    # root.attributes('-fullscreen', True)
    root.mainloop()


class AnomTestPage(TK.Frame):
    def __init__(self, parent):
        TK.Frame.__init__(self, parent)
        self.parent = parent
        self.testNumber = 0
        self.totalTests = 12
        self.testColors = [[31, 255],[255, 99],[112, 255],[255, 173],[179, 255],\
                [210, 255],[155, 239],[255, 207],[146, 255],[255, 137],\
                [74, 255],[255, 57],[240, 255]]
        self.userColors = []
        self.initUI()


    def initUI(self):
        self.parent.title('NoColorBlind')
        customFont1 = tkFont.Font(family = 'Helvetica', size = 40, weight = 'bold')
        customFont2 = tkFont.Font(family = 'Times', size = 25, weight = 'bold')

        self.titleLabel = TK.Frame(self.parent)
        self.titleLabel.pack(side = TK.TOP)
        self.titleLabel.label = TK.Label(self.titleLabel, width = 160, pady = 20,\
            text = 'No Color Blind ', font = customFont1, fg = '#5cb85c', bg = '#333')
        self.titleLabel.label.pack(expand = 'no')

        self.introLabel = TK.Frame(self.parent)
        self.introLabel.place(x = 280, y = 125)
        self.introLabel.label = TK.Label(self.introLabel, text = 
            '''Please move the scroll bar below to make the right color match the left one,
\nand if you cannot make a match, please choose no match ''')
        self.introLabel.label.pack()
                
        self.color1 = '#%02x%02x%02x' % (self.testColors[self.testNumber][0], \
                self.testColors[self.testNumber][1], 0)
        self.imageLabel1 = TK.Frame(self.parent)
        self.imageLabel1.place(x = 150, y = 200)
        self.imageLabel1.label = TK.Label(self.imageLabel1, width = 40, height = 15, bg = self.color1)
        self.imageLabel1.label.pack()

        self.intRG = TK.IntVar()
        # self.color2 = '#%02x%02x%02x' % (self.intRG.get(), self.intRG.get(), 0)
        self.imageLabel2 = TK.Frame(self.parent)
        self.imageLabel2.place(x = 500, y = 200)
        self.imageLabel2.label = TK.Label(self.imageLabel2, width = 40, height = 15)
        self.imageLabel2.label.pack()

        self.scale = TK.Scale(self.parent, from_ = 99, to = 255, length = 250, \
                orient = TK.HORIZONTAL, command = self.onScaleChange)
        self.scale.place(x = 520, y = 450)

        self.matchBtn = TK.Frame(self.parent)
        self.matchBtn.place(x = 800, y = 250)
        self.matchBtn.button = TK.Button(self.matchBtn, width = 10, height = 1, \
                text = 'Match', font = customFont2)
        self.matchBtn.button.bind('<Button-1>', self.matchBtnClicked)
        self.matchBtn.button.pack()

        self.noMatchBtn = TK.Frame(self.parent)
        self.noMatchBtn.place(x = 800, y = 350)
        self.noMatchBtn.button = TK.Button(self.noMatchBtn, width = 10, height = 1, \
                text = 'No Match', font = customFont2)
        self.noMatchBtn.button.bind('<Button-1>', self.noMatchBtnClicked)
        self.noMatchBtn.button.pack()


    def onScaleChange(self, val):
        v = int(float(val))
        # print v
        self.intRG.set(v)
        self.color2 = '#%02x%02x%02x' % (self.intRG.get(), self.intRG.get(), 0)
        self.imageLabel2.label.configure(background = self.color2)

    def matchBtnClicked(self, event):
        # print self.testNumber
        if self.testNumber < 12:
            self.color1 = '#%02x%02x%02x' % (self.testColors[self.testNumber + 1][0], \
                self.testColors[self.testNumber + 1][1], 0)
            self.imageLabel1.label.configure(background = self.color1)
            self.userColors.append([self.testNumber, self.intRG.get()])
            self.testNumber += 1
        elif self.testNumber == 12:
            self.userColors.append([13, self.intRG.get()])
            result = tkMessageBox.askquestion("Finished Anomaloscope Test", "Ready for the result???")
            if result == 'yes':
                # resultWindow = TK.Toplevel(self.parent)                
                # resultPage = ResultPage(resultWindow)
                # resultPage.showCamera()
                resultPageCV = ResultPageCV(self.userColors)
                resultPageCV.parseResult()
                resultPageCV.showCamera()
                print 'yes'
                
            else:
                print 'no'
        else:
            tkMessageBox.showinfo("Finished Anomaloscope Test", "Result page already shown")
        
        
    def noMatchBtnClicked(self, event):
        if self.testNumber < 12:
            self.color1 = '#%02x%02x%02x' % (self.testColors[self.testNumber + 1][0], \
                self.testColors[self.testNumber + 1][1], 0)
            self.imageLabel1.label.configure(background = self.color1)
            self.testNumber += 1 
        elif self.testNumber == 12:
            result = tkMessageBox.askquestion("Finished Anomaloscope Test", "Ready for the result???")
            if result == 'yes':
                
                resultPageCV = ResultPageCV(self.userColors)
                resultPageCV.parseResult()
                resultPageCV.showCamera()
                print 'yes'
                
            else:
                print 'no'
        else:
            tkMessageBox.showinfo("Finished Anomaloscope Test", "Result page already shown") 







# if __name__ == '__main__':
#     main()