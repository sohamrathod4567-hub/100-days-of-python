from tkinter import *
THEME_COLOR = "#375362"
FONT = ("Arial" , 20 , "italic")

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.text = Label(text="Score : 0",bg=THEME_COLOR,fg="white" , font=("Arial" , 10 , "bold"))
        self.text.grid(row=0, column=1)



        self.canvas = Canvas(width=250, height=300, bg="white")
        self.canvas.create_text( 125 ,  150, text = "Pablo" , font= FONT)
        self.canvas.grid(row=1, column=0,columnspan=2)


        self.window.mainloop()
