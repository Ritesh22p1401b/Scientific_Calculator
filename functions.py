from tkinter import *




# Click Function
def click(event):
    # global scvalue
    from main import screen,scvalue
    text = event.widget.cget("text")
    screen.insert(0, text) 

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


