from tkinter import * # Import tkinter library

window = Tk()

window.title("Welcome to my first tkinter app")
window.geometry('550x300')

lbl = Label(window, text="How are you doing?", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)

txt = Entry(window, width=20)
txt.grid(column=0, row=2)

def click():
    res = "Welcome " + txt.get() 
    lbl.configure(text= res)

btn = Button(window, text="Click me", command=click)
btn.grid(column=0, row=4)

window.mainloop()

