import tkinter as tk
from tkinter import *




#creating tkinter or software main window.
window=tk.Tk()
window.title("Scientific Calculator")
window.geometry("490x570")


# Create a frame
frame = Frame(window, width=375, height=475, bg="white",borderwidth=2,
highlightbackground="black", highlightcolor="black", highlightthickness=2)
frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
frame.pack(expand=True)  # Center the frame in the window


def click(event):
    
    global scvalue
    text = event.widget.cget("text")
    #screen.insert(0, text) 

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






#Creating Screen and entering the value
scvalue = StringVar()

screen = Entry(frame, textvar=scvalue, font="lucida 20 bold",relief=SUNKEN,borderwidth=2)
screen.pack(fill=X,ipadx=6,pady=8,padx=10) #padding of screen
scvalue.set("")




# creating button of calculator
b9 = Button(frame, text="9", padx=6, pady=1, font="lucida 15 bold",bg="lightblue") # design of button
b9.place(relx=1.0, x=-5,y=80, anchor='ne') # placement of button 
b9.bind("<Button-1>",click)

b8 = Button(frame, text="8", padx=6, pady=1, font="lucida 15 bold",bg="lightblue")
b8.place(relx=1.0, x=-50,y=80, anchor='ne')
b8.bind("<Button-1>",click)


b7 = Button(frame, text="7", padx=6, pady=1, font="lucida 15 bold",bg="lightblue")
b7.place(relx=1.0, x=-100,y=80, anchor='ne')
b7.bind("<Button-1>",click)


b6 = Button(frame, text="6", padx=6, pady=1, font="lucida 15 bold",bg="lightblue")
b6.place(relx=1.0, x=-5,y=130, anchor='ne')
b6.bind("<Button-1>",click)


b5 = Button(frame, text="5", padx=6, pady=1, font="lucida 15 bold",bg="lightblue")
b5.place(relx=1.0, x=-50,y=130, anchor='ne')
b5.bind("<Button-1>",click)


b4 = Button(frame, text="4", padx=6, pady=1, font="lucida 15 bold",bg="lightblue")
b4.place(relx=1.0, x=-100,y=130, anchor='ne')
b4.bind("<Button-1>",click)


b3 = Button(frame, text="3", padx=6, pady=1, font="lucida 15 bold",bg="lightblue")
b3.place(relx=1.0, x=-5,y=180, anchor='ne')
b3.bind("<Button-1>",click)


b2 = Button(frame, text="2", padx=6, pady=1, font="lucida 15 bold",bg="lightblue")
b2.place(relx=1.0, x=-50,y=180, anchor='ne')
b2.bind("<Button-1>",click)


b1 = Button(frame, text="1", padx=6, pady=1, font="lucida 15 bold",bg="lightblue")
b1.place(relx=1.0, x=-100,y=180, anchor='ne')
b1.bind("<Button-1>",click)


b0 = Button(frame, text="0", padx=6, pady=1, font="lucida 15 bold",bg="lightblue")
b0.place(relx=1.0, x=-50,y=230, anchor='ne')
b0.bind("<Button-1>",click)


b = Button(frame, text=".", padx=8, pady=1, font="lucida 15 bold",bg="lightblue")
b.place(relx=1.0, x=-5,y=230, anchor='ne')
b.bind("<Button-1>",click)


ac = Button(frame, text="AC", padx=4, pady=6, font="lucida 11 bold",bg="lightblue")
ac.place(relx=1.0, x=-100,y=230, anchor='ne')
ac.bind("<Button-1>",click)


button = Button(frame, text="*", padx=7, pady=1, font="lucida 15 bold",bg="lightblue")
button.place(relx=1.0, x=-150,y=80, anchor='ne')
button.bind("<Button-1>",click)


button = Button(frame, text="/", padx=8, pady=1, font="lucida 15 bold",bg="lightblue")
button.place(relx=1.0, x=-150,y=130, anchor='ne')
button.bind("<Button-1>",click)


button = Button(frame, text="+", padx=6, pady=1, font="lucida 15 bold",bg="lightblue")
button.place(relx=1.0, x=-150,y=180, anchor='ne')
button.bind("<Button-1>",click)


button = Button(frame, text="=", padx=6, pady=1, font="lucida 15 bold",bg="lightblue")
button.place(relx=1.0, x=-150,y=230, anchor='ne')
button.bind("<Button-1>",click)



















window.mainloop()


