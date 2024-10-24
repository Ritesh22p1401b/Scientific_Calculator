import tkinter as tk
from tkinter import *
from functions import *
switch=None



#creating tkinter or software main window.
window=tk.Tk()
window.title("Scientific Calculator")
window.configure(bg="gray")
window.geometry("490x570")



# Create a frame
frame = Frame(window, width=375, height=475, bg="gray11",borderwidth=2,
highlightbackground="black", highlightcolor="gray11", highlightthickness=2)
frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
frame.pack(expand=True)  # Center the frame in the window





# Functions for calculator.

def close():
    window.destroy()


def clear():
    screen.delete(0,"end")


def backspace():
    screen.delete(screen.index("end")-1)


def press(input):
    length=len(screen.get())
    screen.insert(length,input)


def get_sign(sign,expression):
    value=expression.split(sign,1)
    return value


def convert():
    global switch
    if switch == None:
        switch=True
        conv_button['text']="Deg"
    else:
        switch=None
        conv_button['text']="Rad"





    
def equal():
    expression=screen.get()
    clear()
    try:

        if expression.find("(")>0:
            data=get_sign("(",expression)
            answer=scientific_cal(data[0],data[1])
        

        elif expression.find("*")>0:
            data=get_sign("*",expression)
            answer=multiply(data[0],data[1])


        elif expression.find("+")>0:
            data=get_sign("+",expression)
            answer=add(data[0],data[1])


        elif expression.find("-")>0:
            data=get_sign("-",expression)
            answer=sub(data[0],data[1])


        elif expression.find("/")>0:
            data=get_sign("/",expression)
            answer=divide(data[0],data[1])


        elif expression.find("√")>0:
            data=get_sign("√",expression)
            answer=root(data[0])


        elif expression.find("P")>0:
            data=get_sign("P",expression)
            answer=permutation(data[0],data[1])


        elif expression.find("C")>0:
            data=get_sign("C",expression)
            answer=combination(data[0],data[1])


        elif expression.find("^")>0:
            data=get_sign("^",expression)
            answer=power(data[0],data[1])


        elif expression.find("%")>0:
            data=get_sign("%",expression)
            answer=remainder_fuc(data[0],data[1])


        elif expression.find("!")>0:
            data=get_sign("!",expression)
            answer=fac(data[0],data[1])


        elif expression.find("π")==0:
            answer=m.pi


        elif expression.find("e")==0:
            answer=m.e



        screen.insert(0,answer)


    except:
        screen.insert(0,"Error")












#fonts 
font=("Times New Roman Greek",14)

#Creating Screen and entering the value
scvalue = StringVar()
screen = Entry(frame, textvar=scvalue, font=font,relief=SUNKEN,borderwidth=2)
screen.pack(fill=X,ipadx=6,pady=8,padx=10) #padding of screen
scvalue.set("")





# creating button of calculator
b9 = Button(frame, text="9", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press(9)) # design of button
b9.place(relx=1.0, x=-5,y=80, anchor='ne') # placement of button 


b8 = Button(frame, text="8", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press(8))
b8.place(relx=1.0, x=-45,y=80, anchor='ne')


b7 = Button(frame, text="7", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press(7))
b7.place(relx=1.0, x=-85,y=80, anchor='ne')


b6 = Button(frame, text="6", padx=6, pady=1,  font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press(6))
b6.place(relx=1.0, x=-5,y=130, anchor='ne')


b5 = Button(frame, text="5", padx=6, pady=1,  font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press(5))
b5.place(relx=1.0, x=-45,y=130, anchor='ne')


b4 = Button(frame, text="4", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press(4))
b4.place(relx=1.0, x=-85,y=130, anchor='ne')


b3 = Button(frame, text="3", padx=6, pady=1, font=font,bg="gray1" ,foreground="DarkOrange1",
            command=lambda:press(3))
b3.place(relx=1.0, x=-5,y=180, anchor='ne')


b2 = Button(frame, text="2", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press(2))
b2.place(relx=1.0, x=-45,y=180, anchor='ne')


b1 = Button(frame, text="1", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press(1))
b1.place(relx=1.0, x=-85,y=180, anchor='ne')


b0 = Button(frame, text="0", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press(0))
b0.place(relx=1.0, x=-45,y=230, anchor='ne')


b = Button(frame, text=".", padx=9, pady=1,  font=font,bg="gray1",foreground="DarkOrange1",
           command=lambda:press("."))
b.place(relx=1.0, x=-5,y=230, anchor='ne')


button = Button(frame, text="-", padx=9, pady=1,  font=font,bg="gray1",foreground="DarkOrange1",
                command=lambda:press("-"))
button.place(relx=1.0, x=-85,y=230, anchor='ne')


button = Button(frame, text="%", padx=4.8, pady=1,  font=font,bg="gray1",foreground="DarkOrange1",
                command=lambda:press("%"))
button.place(relx=1.0, x=-125,y=230, anchor='ne')


button = Button(frame, text="*", padx=9, pady=1, font=font,bg="gray1",foreground="DarkOrange1",
                command=lambda:press("*"))
button.place(relx=1.0, x=-125,y=80, anchor='ne')


button = Button(frame, text="/", padx=10, pady=1,  font=font,bg="gray1",foreground="DarkOrange1",
                command=lambda:press("/"))
button.place(relx=1.0, x=-125,y=130, anchor='ne')


button = Button(frame, text="+", padx=7, pady=1,  font=font,bg="gray1",foreground="DarkOrange1",
                command=lambda:press("+"))
button.place(relx=1.0, x=-125,y=180, anchor='ne')


button = Button(frame, text="tan", padx=5, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("tan("))
button.place(relx=1.0,x=-180,y=80, anchor='ne')


button = Button(frame, text="sin", padx=5, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("sin("))
button.place(relx=1.0,x=-180,y=130, anchor='ne')


button = Button(frame, text="cos", padx=2, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("cos("))
button.place(relx=1.0,x=-180,y=180, anchor='ne')


button = Button(frame, text="log", padx=3, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("log("))
button.place(relx=1.0,x=-230,y=80, anchor='ne')


button = Button(frame, text="ln", padx=9, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("ln("))
button.place(relx=1.0,x=-230,y=130, anchor='ne')


button = Button(frame, text="√", padx=10, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("√("))
button.place(relx=1.0,x=-230,y=180, anchor='ne')


button = Button(frame, text="(", padx=13, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("("))
button.place(relx=1.0,x=-230,y=230, anchor='ne')


button = Button(frame, text=")", padx=14, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press(")"))
button.place(relx=1.0,x=-180,y=230, anchor='ne')


button = Button(frame, text="X^ʸ", padx=6, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("^"))
button.place(relx=1.0,x=-278,y=80, anchor='ne')


button = Button(frame, text="y√X", padx=2, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("√"))
button.place(relx=1.0,x=-278,y=130, anchor='ne')


button = Button(frame, text="nPr", padx=4, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("P"))
button.place(relx=1.0,x=-278,y=180, anchor='ne')


button = Button(frame, text="nCr", padx=4, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("C"))
button.place(relx=1.0,x=-278,y=230, anchor='ne')


button = Button(frame, text="tanˉ¹", padx=-2, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("tanˉ¹("))
button.place(relx=1.0,x=-180,y=280, anchor='ne')


button = Button(frame, text="sinˉ¹", padx=-2, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("sinˉ¹("))
button.place(relx=1.0,x=-232,y=280, anchor='ne')


button = Button(frame, text="cosˉ¹", padx=-2, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("cosˉ¹("))
button.place(relx=1.0,x=-285,y=280, anchor='ne')


button = Button(frame, text="log2", padx=-2, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("log2("))
button.place(relx=1.0,x=-5,y=280, anchor='ne')


button = Button(frame, text="π", padx=-2, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("π"))
button.place(relx=1.0,x=-60,y=280, anchor='ne')


button = Button(frame, text="e", padx=-2, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("e"))
button.place(relx=1.0,x=-90,y=280, anchor='ne')



button = Button(frame, text="X!", padx=-2, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:press("!"))
button.place(relx=1.0,x=-118,y=280, anchor='ne')



conv_button = Button(frame,text="Rad",padx=2, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=convert)
conv_button.place(relx=1.0,x=-260,y=330, anchor='ne')






button = Button(frame, text="=", padx=47, pady=1,  font=font,bg="DarkOrange1",foreground="white",command=equal)
button.place(relx=1.0, x=-5,y=330, anchor='ne')


button = Button(frame, text="B", padx=47, pady=1,  font=font,bg="gray1",foreground="DarkOrange1",command=backspace)
button.place(relx=1.0, x=-125,y=330, anchor='ne')


ac = Button(frame, text="AC", padx=1, pady=2,  font=font,bg="gray1",foreground="DarkOrange1",command=clear)
ac.place(relx=1.0, x=-180,y=400, anchor='ne')


button = Button(frame, text="Close", padx=10, pady=2,  font=font,bg="gray1",foreground="DarkOrange1",command=close)
button.place(relx=1.0, x=-5,y=400, anchor='ne')







window.mainloop()
