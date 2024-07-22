from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which color will win the race?  Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

tim = Turtle(shape='turtle')
tim.color(colors[0])
tim.penup()
tim.goto(x=-230, y=100)

tod = Turtle(shape='turtle')
tod.color(colors[1])
tod.penup()
tod.goto(x=-230, y=60)

tammy = Turtle(shape='turtle')
tammy.color(colors[2])
tammy.penup()
tammy.goto(x=-230, y=20)

tina = Turtle(shape='turtle')
tina.color(colors[3])
tina.penup()
tina.goto(x=-230, y=-20)

trey = Turtle(shape='turtle')
trey.color(colors[4])
trey.penup()
trey.goto(x=-230, y=-60)

tom = Turtle(shape='turtle')
tom.color(colors[5])
tom.penup()
tom.goto(x=-230, y=-100)

screen.exitonclick()
