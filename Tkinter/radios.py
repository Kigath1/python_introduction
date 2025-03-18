from tkinter import * 
window = Tk()  

window.title("Radio Buttons")
window.geometry("600x300")

Products = [
    ("Car", "Car"),
    ("Factory", "Factory")
    ("Money", "Money")
    ("Catalogue", "Catalogue")
    ("School", "School")
    ("Market", "Market")
]

choise = StringVar()
choise.set("Car")

for text,mode in Products: 
    Radiobutton(window, text=text, variable = choise, value = mode).pack(anchor='w')

def clicked(value):
    myLable = Label(window, text = value)
    myLable.pack()

myButton = Button(window, text='Click here', command= lambda: clicked(choise.get()))
myButton.pack

window.mainloop()