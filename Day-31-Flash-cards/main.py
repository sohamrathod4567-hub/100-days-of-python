from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(to_learn)
    card_canvas.itemconfig(card_title, text = "French")
    card_canvas.itemconfig(card_word, text = current_card["French"])





#Set up the screen
screen = Tk()
screen.title("Flashy")
screen.configure(padx=50 , pady=50 , bg=BACKGROUND_COLOR)

#set up the initial canvas
card_canvas = Canvas(width=800 , height=526,background=BACKGROUND_COLOR,highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
card_canvas.create_image(400 , 263 ,image=front_image)
card_title = card_canvas.create_text(400 , 150,text="Title" , font=("Ariel",40,"italic"))
card_word = card_canvas.create_text(400 , 263,text="word" , font=("Ariel",60,"bold"))

card_canvas.grid(row=0, column=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,command= next_card )
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image , command= next_card )
known_button.grid(row=1, column=1)

next_card()
screen.mainloop()