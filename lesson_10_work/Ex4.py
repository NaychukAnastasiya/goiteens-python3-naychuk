from random import choice, random
from turtle import *
from freegames import vector

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])

# початкові координати появи м'яча
ball = vector(0, 0)
# м'яч має рандомний напрямок, який генерується з функції value
aim = vector(value(), value())
state = {1: 0, 2: 0}

def move(player, change):
    "Move player position by change."
    state[player] += change

def rectangle(x, y, width, height):
    "Draw rectangle at (x, y) with given width and height."
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw():
    "Draw game and move pong ball."
    clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    # розмір м'яча
    dot(30)
    update()
    # границі
    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return
    # швидкість руху м'яча
    ontimer(draw, 20)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# клавіші управління
onkey(lambda: move(1, 80), 'w')
onkey(lambda: move(1, -80), 's')
onkey(lambda: move(2, 80), 'i')
onkey(lambda: move(2, -80), 'k')
draw()
done()