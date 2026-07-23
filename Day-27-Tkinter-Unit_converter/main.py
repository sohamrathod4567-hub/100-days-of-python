import tkinter
def button_clicked():
    my_label["text"]=input.get()
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 25))
my_label.grid(column=0, row=0)

#Button
new_button = tkinter.Button(text="No piki pani")
new_button.grid(column=2, row=0)
button = tkinter.Button(text="Hola", command=button_clicked)
button.grid(column=1, row=1)

#Entry
input = tkinter.Entry(width=10)
input.get()
input.grid(column=4, row=4)






window.mainloop()
