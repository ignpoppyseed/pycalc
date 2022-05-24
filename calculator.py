from tkinter import *

#creating window
calc = Tk()

#creating frames to hold buttons 
row1 = Frame(calc)
row2 = Frame(calc)
row3 = Frame(calc)
row4 = Frame(calc)
row5 = Frame(calc)

#window configuration
calc.title("PyCalc")
calc.geometry("205x200")
toplabel = Label(calc, text="")
toplabel.pack(side=TOP, fill=BOTH, expand=True)

#creating equation variable
op = ""

def key(num): #function to handle buttonpresses
    global op #pulling equation variable into function
    op = op + str(num) #appending new buttonpress to equation
    toplabel.config(text = op) #edit label to reflect updated equation
def equals(): #function that executes when the = button is pressed
    try:
        global op #pulling equation variable into function
        total = str(eval(op)) #evaluate the operation, make it a string (text) and assign it to new variable "total"
        toplabel.config(text = total) #change label to answer
        op = "" #reset equation to zero
    except:
        toplabel.config(text="ERROR!") #set label to error if equation fails
        op = "" #reset equation to zero
def leave(): #function to exit calculator
    calc.destroy() #destroys calculator window
def clear():#function
    global op #pulling equation variable into function
    op = "" #reset equation to zero
    toplabel.config(text="") #edit label to reflect updated equation

# this is the "button second" (ooo fun) its basically the same code over and over again
btn7 = Button(row1, text="7", width=2, command=lambda: key(7)) # creates a button with text on it. the command part sends information to the key function
btn7.pack(side=LEFT, fill=BOTH, expand=True) # uses the pack function to place the button and sets it to expand with the window
btn8 = Button(row1, text="8", width=2, command=lambda: key(8))
btn8.pack(side=LEFT, fill=BOTH, expand=True)
btn9 = Button(row1, text="9", width=2, command=lambda: key(9))
btn9.pack(side=LEFT, fill=BOTH, expand=True)
btndiv = Button(row1, text="÷", width=2, command=lambda: key("/"))
btndiv.pack(side=LEFT, fill=BOTH, expand=True)

btn4 = Button(row2, text="4", width=2, command=lambda: key(4))
btn4.pack(side=LEFT, fill=BOTH, expand=True)
btn5 = Button(row2, text="5", width=2, command=lambda: key(5))
btn5.pack(side=LEFT, fill=BOTH, expand=True)
btn6 = Button(row2, text="6", width=2, command=lambda: key(6))
btn6.pack(side=LEFT, fill=BOTH, expand=True)
btnmu = Button(row2, text="x", width=2, command=lambda: key("*"))
btnmu.pack(side=LEFT, fill=BOTH, expand=True)

btn1 = Button(row3, text="1", width=2, command=lambda: key(1))
btn1.pack(side=LEFT, fill=BOTH, expand=True)
btn2 = Button(row3, text="2", width=2, command=lambda: key(2))
btn2.pack(side=LEFT, fill=BOTH, expand=True)
btn3 = Button(row3, text="3", width=2, command=lambda: key(3))
btn3.pack(side=LEFT, fill=BOTH, expand=True)
btnmi = Button(row3, text="-", width=2, command=lambda: key("-"))
btnmi.pack(side=LEFT, fill=BOTH, expand=True)

btnd = Button(row4, text=".", width=2, command=lambda: key("."))
btnd.pack(side=LEFT, fill=BOTH, expand=True)
btn0 = Button(row4, text="0", width=2, command=lambda: key(0))
btn0.pack(side=LEFT, fill=BOTH, expand=True)
btne = Button(row4, text="=", width=2, command=equals)
btne.pack(side=LEFT, fill=BOTH, expand=True)
btnp = Button(row4, text="+", width=2, command=lambda: key("+"))
btnp.pack(side=LEFT, fill=BOTH, expand=True)

btnclr = Button(row5, text="Clear", command=clear, width=2) #buton to activate clear function
btnclr.pack(side=LEFT, fill=BOTH, expand=True) #uses pack function to place button
btnexit = Button(row5, text="Exit", command=leave, width=2) #buton to activate exit function
btnexit.pack(side=LEFT, fill=BOTH, expand=True) #uses pack function to place button

#places frames for rows 1 - 5
row1.pack(fill=BOTH, expand=True) 
row2.pack(fill=BOTH, expand=True)
row3.pack(fill=BOTH, expand=True)
row4.pack(fill=BOTH, expand=True)
row5.pack(fill=BOTH, expand=True)

#starts window
calc.mainloop()
