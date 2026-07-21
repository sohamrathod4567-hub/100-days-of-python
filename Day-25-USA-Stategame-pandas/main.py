import turtle
import pandas

screen = turtle.Screen()
screen.title("U. S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x , y ):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#
answer_state = screen.textinput(title="Guess the State", prompt="What is another State's name?").lower()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

if  answer_state in all_states:
    print("Correct!")




screen.exitonclick()