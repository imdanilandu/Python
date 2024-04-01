import turtle
fish_scr = turtle
 
def Draw_Fish(i,j):
    fish_scr.penup()
    fish_scr.goto(i,j)
    fish_scr.speed(10)
    fish_scr.left(45)
    fish_scr.pendown()
    fish_scr.forward(100)
    fish_scr.right(135)
    fish_scr.forward(130)
    fish_scr.right(130)
    fish_scr.forward(90)
    fish_scr.left(90)
    fish_scr.right(90)
    fish_scr.circle(200,90)
    fish_scr.left(90)
    fish_scr.circle(200,90)
    fish_scr.penup()
    fish_scr.left(130)
    fish_scr.forward(200)
    fish_scr.pendown()
    fish_scr.circle(10,360)
 
Draw_Fish(0,0)

fish_scr.done()