
from PIL import ImageTk, Image
import Tkinter as TK
import tkFont
import tkMessageBox
from AnomTestPage import AnomTestPage

class IshiTestPage(TK.Frame):
    def __init__(self, parent):
        TK.Frame.__init__(self, parent)
        self.parent = parent
        self.answers = [12, 8, 29, 5, 74, 2, 45, 5, 7, 16, 35, 96]        
        self.testNumber = 0
        self.totalTests = 12
        self.wrongs = 0        
        self.initUI()

    def initUI(self):
        self.parent.title('NoColorBlind')
        customFont1 = tkFont.Font(family = 'Helvetica', size = 40, weight = 'bold')
        customFont2 = tkFont.Font(family = 'Purisa', size = 25, weight = 'bold')

        self.titleLabel = TK.Frame(self.parent)
        self.titleLabel.pack(side = TK.TOP)
        self.titleLabel.label = TK.Label(self.titleLabel, width = 160, pady = 20,\
            text = 'No Color Blind ', font = customFont1, fg = '#5cb85c', bg = '#333')
        self.titleLabel.label.pack(expand = 'no')

        self.imageLabel = TK.Frame(self.parent)
        self.imageLabel.place(x = 150, y = 200)
        self.imagePath = 'img/ishihara_plate' + str(self.testNumber) + '.png'
        plateImage = ImageTk.PhotoImage(Image.open(self.imagePath))
        self.imageLabel.label = TK.Label(self.imageLabel,height = 350, width = 350,\
            image = plateImage, bg = 'black')
        self.imageLabel.label.image = plateImage
        self.imageLabel.label.pack(expand = 'no')

        self.inputLabel = TK.Frame(self.parent)
        self.inputLabel.place(x = 600, y = 200)
        self.inputLabel.label = TK.Label(self.inputLabel, wraplength = 300, text = 'Please type in what you see on the left',\
            font = customFont2, fg = '#5cb85c')
        self.inputLabel.label.pack()
        self.inputLabel.entry = TK.Entry(self.inputLabel, width = 25, justify = TK.CENTER)
        self.inputLabel.entry.pack()

        self.btnLabel = TK.Frame(self.parent)
        self.btnLabel.place(x = 600, y = 500)
        self.btnLabel.button = TK.Button(self.btnLabel, width = 20, height = 1, bd = 5, bg = 'blue',\
         activebackground = 'red', text = 'Next', font = customFont2)
        self.btnLabel.button.bind('<Button-1>', self.nextButtonClicked)
        self.btnLabel.button.pack(expand = 'no')

    
    def nextButtonClicked(self, event):
        if self.testNumber < 11:
            self.imagePath = 'img/ishihara_plate' + str(self.testNumber) + '.png'
            print self.imagePath
            plateImage = ImageTk.PhotoImage(Image.open(self.imagePath))
            self.imageLabel.label.image = plateImage
            self.imageLabel.label.configure(image = plateImage)
            userInput = self.inputLabel.entry.get()
            if userInput != self.answers[self.testNumber]:
                self.wrongs += 1
            self.testNumber += 1
        elif self.testNumber == 11:
            if self.wrongs > 1:
                result = tkMessageBox.askyesno("Sorry", "Looks like there is some deficiency")
                if result == True:
                    for child in self.parent.winfo_children():
                        print child
                        child.destroy()
                    anomTestPage = AnomTestPage(self.parent)
                else:
                    for child in self.parent.winfo_children():
                        print child
                        child.destroy()
                    anomTestPage = AnomTestPage(self.parent)
            else:
                tkMessageBox.showinfo("Finished", "Everything works just fine!")
        else:
            pass



root = TK.Tk()
ishiTestPage = IshiTestPage(root)
# root.configure(background = 'grey')
root.geometry('{}x{}'.format(1000, 700))
# root.attributes('-fullscreen', True)
root.mainloop()