import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("Guess the state.")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states_name = data.state.to_list()

guessed_states = []

while True:
    answers = screen.textinput(
        title=f"{len(guessed_states)}/50 states guessed.Type 'Exit' to exit the game.",
        prompt="What's another state?",
    ).title()
    if answers == "Exit":
        break
    if answers in states_name:
        name = turtle.Turtle()
        name.penup()
        name.hideturtle()
        print(answers)
        thatParticularState = data[data.state == answers]
        name.goto(int(thatParticularState.x), int(thatParticularState.y))
        name.write(answers)
        guessed_states.append(answers)

    if len(guessed_states) == 50:
        break

# not_guessed_states = []
# for ele in data.state.to_list():
#     if ele not in guessed_states:
#         not_guessed_states.append(ele)

not_guessed_states = [ele for ele in data.state.to_list() if ele not in guessed_states]


df = pd.DataFrame(not_guessed_states)
df.to_csv("states_to_learn.csv")
