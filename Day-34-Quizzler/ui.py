from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial" , 20 , "italic")

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain ):
        self.quiz = quiz_brain
        # Made the window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # The Text label
        self.score = Label(text="Score : 0",bg=THEME_COLOR,fg="white" , font=("Arial" , 10 , "bold"))
        self.score.grid(row=0, column=1)


        # This is for the canvas
        self.canvas = Canvas(width=250, height=300, bg="white")
        self.question_text = self.canvas.create_text(
            125 ,
            150 ,
            text = "Pablo" ,
            font= FONT ,
            width= 230
        )
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)


        #Right and Wrong Button
        right_img = PhotoImage(file="Images/true.png")
        self.right = Button(image=right_img , highlightthickness=0 , command= self.is_true)
        self.right.grid(row=2, column=0)

        wrong_img = PhotoImage(file="Images/false.png")
        self.wrong = Button(image=wrong_img , highlightthickness=0 , command= self.is_false)
        self.wrong.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        self.canvas.configure(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="That is the end of your Quiz \n Thank you!")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self , check):
        if check:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000 , self.get_next_question)

