from turtle import Turtle, Screen

image = 'map_europe.gif'

turtle = Turtle()
screen = Screen()
game_on = True

while game_on:
    screen.addshape(image)
    turtle.shape(image)

    screen.listen()

    def get_mouse_click_coor(x, y):
        print(x, y)

    screen.onclick(get_mouse_click_coor)
