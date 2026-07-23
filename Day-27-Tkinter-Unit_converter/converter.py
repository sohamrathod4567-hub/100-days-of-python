import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.geometry("400x300")
window.config(padx=20, pady=20)

#Label
first_label = tkinter.Label(text="is equal to")
first_label.grid(column=0, row=1)

#input
mile = tkinter.Entry(width=10)
mile.get()
mile.grid(column=1, row=0)

#miles
miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

#converter
km = tkinter.Label(text="Km")


#Km
kilo = tkinter.Label(text="Km")
kilo.grid(column=2, row=1)

#calculate
calc = tkinter.Button(text="Calculate")
calc.grid(column=1, row=2)






window.mainloop()