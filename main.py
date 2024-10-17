import tkinter as tk
from tkinter import *


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


def backspace():
    screen.delete(screen.index("end")-1)



def single_operand_function(input):
    length=len(screen.get())
    screen.insert(length,input)



def click(event):
    global scvalue
    text = event.widget.cget("text")
  
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"
        
        scvalue.set(value)
        screen.update()

    elif text == "AC":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()




#fonts 
font=("Times New Roman Greek",14)

#Creating Screen and entering the value
scvalue = StringVar()
screen = Entry(frame, textvar=scvalue, font=font,relief=SUNKEN,borderwidth=2)
screen.pack(fill=X,ipadx=6,pady=8,padx=10) #padding of screen
scvalue.set("")



# creating button of calculator

b9 = Button(frame, text="9", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1") # design of button
b9.place(relx=1.0, x=-5,y=80, anchor='ne') # placement of button 
b9.bind("<Button-1>",click)

b8 = Button(frame, text="8", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1")
b8.place(relx=1.0, x=-45,y=80, anchor='ne')
b8.bind("<Button-1>",click)


b7 = Button(frame, text="7", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1")
b7.place(relx=1.0, x=-85,y=80, anchor='ne')
b7.bind("<Button-1>",click)


b6 = Button(frame, text="6", padx=6, pady=1,  font=font,bg="gray1",foreground="DarkOrange1")
b6.place(relx=1.0, x=-5,y=130, anchor='ne')
b6.bind("<Button-1>",click)


b5 = Button(frame, text="5", padx=6, pady=1,  font=font,bg="gray1",foreground="DarkOrange1")
b5.place(relx=1.0, x=-45,y=130, anchor='ne')
b5.bind("<Button-1>",click)


b4 = Button(frame, text="4", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1")
b4.place(relx=1.0, x=-85,y=130, anchor='ne')
b4.bind("<Button-1>",click)


b3 = Button(frame, text="3", padx=6, pady=1, font=font,bg="gray1" ,foreground="DarkOrange1")
b3.place(relx=1.0, x=-5,y=180, anchor='ne')
b3.bind("<Button-1>",click)


b2 = Button(frame, text="2", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1")
b2.place(relx=1.0, x=-45,y=180, anchor='ne')
b2.bind("<Button-1>",click)


b1 = Button(frame, text="1", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1")
b1.place(relx=1.0, x=-85,y=180, anchor='ne')
b1.bind("<Button-1>",click)


b0 = Button(frame, text="0", padx=6, pady=1, font=font,bg="gray1",foreground="DarkOrange1" )
b0.place(relx=1.0, x=-45,y=230, anchor='ne')
b0.bind("<Button-1>",click)


b = Button(frame, text=".", padx=9, pady=1,  font=font,bg="gray1",foreground="DarkOrange1")
b.place(relx=1.0, x=-5,y=230, anchor='ne')
b.bind("<Button-1>",click)


button = Button(frame, text="-", padx=9, pady=1,  font=font,bg="gray1",foreground="DarkOrange1")
button.place(relx=1.0, x=-85,y=230, anchor='ne')
button.bind("<Button-1>",click)


button = Button(frame, text="%", padx=4.8, pady=1,  font=font,bg="gray1",foreground="DarkOrange1")
button.place(relx=1.0, x=-125,y=230, anchor='ne')
button.bind("<Button-1>",click)


button = Button(frame, text="*", padx=9, pady=1, font=font,bg="gray1",foreground="DarkOrange1")
button.place(relx=1.0, x=-125,y=80, anchor='ne')
button.bind("<Button-1>",click)


button = Button(frame, text="/", padx=10, pady=1,  font=font,bg="gray1",foreground="DarkOrange1")
button.place(relx=1.0, x=-125,y=130, anchor='ne')
button.bind("<Button-1>",click)


button = Button(frame, text="+", padx=7, pady=1,  font=font,bg="gray1",foreground="DarkOrange1")
button.place(relx=1.0, x=-125,y=180, anchor='ne')
button.bind("<Button-1>",click)


button = Button(frame, text="=", padx=47, pady=1,  font=font,bg="gray1",foreground="DarkOrange1")
button.place(relx=1.0, x=-5,y=280, anchor='ne')
button.bind("<Button-1>",click)


button = Button(frame, text="B", padx=47, pady=1,  font=font,bg="gray1",foreground="DarkOrange1",command=backspace)
button.place(relx=1.0, x=-125,y=280, anchor='ne')


button = Button(frame, text="tan", padx=5, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:single_operand_function("tan("))
button.place(relx=1.0,x=-180,y=80, anchor='ne')


button = Button(frame, text="sin", padx=5, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:single_operand_function("sin("))
button.place(relx=1.0,x=-180,y=130, anchor='ne')


button = Button(frame, text="cos", padx=2, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:single_operand_function("cos("))
button.place(relx=1.0,x=-180,y=180, anchor='ne')


button = Button(frame, text="log", padx=3, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:single_operand_function("log("))
button.place(relx=1.0,x=-230,y=80, anchor='ne')


button = Button(frame, text="ln", padx=9, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:single_operand_function("ln("))
button.place(relx=1.0,x=-230,y=130, anchor='ne')


button = Button(frame, text="sqrt", padx=0, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:single_operand_function("sqrt("))
button.place(relx=1.0,x=-230,y=180, anchor='ne')


button = Button(frame, text="(", padx=13, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:single_operand_function("("))
button.place(relx=1.0,x=-230,y=230, anchor='ne')


button = Button(frame, text=")", padx=14, pady=1,font=font,bg="gray1",foreground="DarkOrange1",
            command=lambda:single_operand_function(")"))
button.place(relx=1.0,x=-180,y=230, anchor='ne')












ac = Button(frame, text="AC", padx=1, pady=2,  font=font,bg="gray1",foreground="DarkOrange1")
ac.place(relx=1.0, x=-180,y=380, anchor='ne')
ac.bind("<Button-1>",click)


button = Button(frame, text="Close", padx=10, pady=2,  font=font,bg="gray1",foreground="DarkOrange1",command=close)
button.place(relx=1.0, x=-5,y=380, anchor='ne')








window.mainloop()
