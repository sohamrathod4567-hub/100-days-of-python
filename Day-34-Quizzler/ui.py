from tkinter import *

from PIL.ImageOps import pad

THEME_COLOR = "#375362"
FONT = ("Arial" , 20 , "italic")

class QuizInterface:

    def __init__(self):
        # Made the window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # The Text label
        self.text = Label(text="Score : 0",bg=THEME_COLOR,fg="white" , font=("Arial" , 10 , "bold"))
        self.text.grid(row=0, column=1)


        # This is for the canvas
        self.canvas = Canvas(width=250, height=300, bg="white")
        self.canvas.create_text( 125 ,  150, text = "Pablo" , font= FONT)
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)


        #Right and Wrong Button
        right_img = PhotoImage(file="Images/true.png")
        self.right = Button(image=right_img , highlightthickness=0)
        self.right.grid(row=2, column=0)

        wrong_img = PhotoImage(file="Images/false.png")
        self.wrong = Button(image=wrong_img , highlightthickness=0)
        self.wrong.grid(row=2, column=1)


        self.window.mainloop()
