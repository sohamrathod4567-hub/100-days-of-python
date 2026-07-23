import tkinter
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 25))
my_label.pack()

#Button

def button_clicked():
    my_label["text"]=input.get()
button = tkinter.Button(text="Hola", command=button_clicked)
button.pack()

#Entry
input = tkinter.Entry(width=10)
input.pack()
input.get()






window.mainloop()
