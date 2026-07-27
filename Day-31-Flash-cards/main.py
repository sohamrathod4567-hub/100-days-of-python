from tkinter import *

from pandas.core.interchange import column
from wcwidth import width

BACKGROUND_COLOR = "#B1DDC6"

#Set up the screen
screen = Tk()
screen.title("Flashy")
screen.configure(padx=50 , pady=50 ,  bg=BACKGROUND_COLOR)

#set up the initial canvas
card_canvas = Canvas(width=800 , height=526,background=BACKGROUND_COLOR,highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
card_canvas.create_image(400 , 263 ,image=front_image)
card_canvas.create_text(400 , 150,text="Title" , font=("Ariel",40,"italic"))
card_canvas.create_text(400 , 263,text="word" , font=("Ariel",60,"bold"))

card_canvas.grid(row=0, column=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image )
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image)
known_button.grid(row=1, column=1)

screen.mainloop()