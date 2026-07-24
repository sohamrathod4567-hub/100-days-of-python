from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_l.config(text="Timer",bg=YELLOW,fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60

    if reps % 8 == 0 :
        count_down(long_break_sec)
        timer_l.config(text="Break",bg=YELLOW,fg=RED)
    elif reps % 2 == 0 :
        count_down(short_break_sec)
        timer_l.config(text="Break",bg=YELLOW,fg=PINK)
    else:
        count_down(work_sec)
        timer_l.config(text="Work",bg=YELLOW,fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10 :   # This is an example of Dynamic typing
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000 , count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions) :
            mark += "✔"
            check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
#window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50 ,bg=YELLOW)

#Canvas for the image
canvas = Canvas(width=200 , height=224 , bg=YELLOW , highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,135,text = "00:00",fill="white",font= (FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

#Label for the timer " TIMER"
timer_l = Label(text="Timer",bg=YELLOW,fg=GREEN , font=(FONT_NAME,35 , "bold"))
timer_l.grid(row=0,column=1)


#Start Button
start = Button(text="Start" , font=(FONT_NAME , 9 , "bold") , command=start_timer)
start.grid(row=2,column=0)

#Reset Button
reset = Button(text="Reset" , font=(FONT_NAME , 9 , "bold"),command=reset_timer)
reset.grid(row=2,column=2)

#check mark
check_mark = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,15))
check_mark.grid(row=3,column=1)


window.mainloop()