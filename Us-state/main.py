import turtle

import pandas

s = turtle.Screen()
s.title("us.states")
image = "blank_states_img.gif"
s.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_ans = []

while len(guessed_ans) < 50:
    ans = s.textinput(title=f"{len(guessed_ans)}/50 States", prompt="give a state name to go").title()

    if ans in all_states:
        t = turtle.Turtle()
        guessed_ans.append(ans)
        t.hideturtle()
        t.penup()
        state = data[data.state == ans]
        t.goto(int(state.x), int(state.y))
        t.write(ans)


s.exitonclick()