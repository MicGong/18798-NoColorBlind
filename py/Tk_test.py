
import Tkinter

def showStr(event = None):
    print (buttonStr.get())


# root = Tkinter.Tk()

# label = Tkinter.Label(root, text = 'NoColorBlind')

# entry = Tkinter.Entry(root)

# label.pack(side = Tkinter.TOP)
# entry.pack()

# root.mainloop()

def newWindow(event, prevWindow):
    top = Tkinter.Toplevel()
    top.title("What about this?")
    
    msg = Tkinter.Message(top, text = 'Hahahaahaha')
    msg.pack()
    
    btn = Tkinter.Button(top, text = 'Dismiss', command = top.destroy)
    btn.pack()


root2 = Tkinter.Tk()
label2 = Tkinter.Label(root2, text = 'please choose a button')

buttonStr = Tkinter.StringVar()

buttonA = Tkinter.Radiobutton(root2, text = 'Button A', variable = buttonStr, value = 'Button A string')
buttonB = Tkinter.Radiobutton(root2, text = 'Button B', variable = buttonStr, value = 'Button B string')
buttonC = Tkinter.Radiobutton(root2, text = 'Button C', variable = buttonStr, value = 'Button C string')

buttonA.config(command = showStr)
buttonB.config(command = showStr)
buttonC.config(command = newWindow(None, root2))

label2.grid(column = 0, row = 0)
buttonA.grid(column = 0, row = 1)
buttonB.grid(column = 0, row = 2)
buttonC.grid(column = 0, row = 3)

buttonA.select()




root2.mainloop()

