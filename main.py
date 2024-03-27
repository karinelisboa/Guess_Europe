from turtle import Turtle, Screen
import pandas as pd

image = 'map_europe.gif'

turtle = Turtle()
screen = Screen()
game_on = True
list_countries = []
guessed_countries = []
not_guessed = []

data = pd.read_csv('some_countries.csv')

for country in data.states:
    list_countries.append(country)

while game_on:
    screen.addshape(image)
    turtle.shape(image)

    screen.listen()

    def get_mouse_click_coor(x, y):
        print(x, y)

    answer = screen.textinput(f"{len(guessed_countries)}/{len(list_countries)}", "Guess a european country:")

    if answer.title() == "Exit":
        not_guessed = [country for country in list_countries if country not in guessed_countries]
        print(f"Countries missed: {not_guessed}")
        game_on = False


    if answer.title() in list_countries:
        guessed_countries.append(answer.title())
        country = Turtle()
        country.hideturtle()
        country.penup()
        country_data = data[data.states == answer.title()]
        country.goto(int(country_data['x']), int(country_data['y']))
        country.write(f"{answer.title()}")

    screen.onclick(get_mouse_click_coor)
