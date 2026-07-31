from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=250, height=300, bg="white")
        self.canvas.create_text( 125 ,  150, text = "Pablo" , font= ("Arial" , 20 , "italic"))
        self.canvas.grid(row=0, column=0)


        self.window.mainloop()
