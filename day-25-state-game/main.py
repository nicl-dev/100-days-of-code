import pandas
import turtle

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
background = "blank_states_img.gif"
screen.addshape(background)
turtle.shape(background)
turtle.penup()
turtle.tracer(0)
df = pandas.read_csv("50_states.csv")
score = 0
all_states = df.state.to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()
    while answer_state in correct_guesses:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="You already guessed that "
                                                                                   "state.\nWhat's another state "
                                                                                   "name?").title()
    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in correct_guesses]
        missed_states = pandas.DataFrame(missed_states)
        missed_states.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        score += 1
        correct_guesses.append(answer_state)
        turtle.setpos(x=int(df[df.state == answer_state].x), y=int(df[df.state == answer_state].y))
        turtle.write(answer_state)
