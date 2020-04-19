# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:15:51 2020

@author: Jeffrey Vickroy
"""
# Vickroy_HW4
# this code demenstrate how a ball of some mass will achieve terminal velocity 
# after enough time. ie once the force of gravity is balanced by air resistance
# I also allow for different cases between elastic and inelastic collisions
# and ask the user how many bounces theyd like to see

## Libraries ##
import turtle
import matplotlib.pyplot as plt

## start up ##
num = float(input('There will be a plot available in the plots pane.\
                  \n\nHow many bounces would you like to see? * '))
conservation = str(input('Would you like your collision to be elastic or inelastic? * '))
m = float(input('How massive is the ball in kg? * '))

## functions ##
def cons(ans):
    if ans == 'elastic': # elastic implies no energy loss in ball
        val = 1
    if ans == 'inelastic': # inelastic implies energy loss to vibrations, heat, etc.
        val = 0.8
    return val

## variables ##
# Fg = m*g (gravity); Fd = b*v**2 (air resistance); a = F / m = g + (b/m)*v**2
g = 9.81 # m/s**2 (gravitational acceleration)
b = 0.01 # N*s**2/m**2 (drag force coefficient)
v = 0 # initial velocity
y = 20; ylist = [y]
x = 10
t = 0; dt = 0.01; tlist = [t]
bounce = 0
loss = cons(conservation) # call function for type of collision

## window settings ##
# makes the window
wn = turtle.Screen()
wn.setup(width = 800, height = 800) # may vary depending on computer screen
wn.bgcolor('white')
wn.setworldcoordinates(-0, -5, 25, 25)

## drawing ##
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.setpos(-5, -0.3)
pen.fillcolor('grey')
pen.begin_fill() # this will start to fill the shaped outlined by the for loop
for i in range(4): # runs the path 4 times to make a square
  pen.forward(40) # move the pen forward 40 pixels
  pen.right(90) # reorient the pen 90 degrees
pen.end_fill()

## make ball ##
ball = turtle.Turtle()
ball.hideturtle()
ball.penup()
ball.shape('circle')
ball.color('black')
ball.setpos(x, y)
ball.stamp() # want to show initial position
ball.color('green')
ball.showturtle()

while bounce <= num:
    ag = -g # accel due to grav
    ad = (b / m)*(v**2)  # accel due to air 
    a = ag + ad # net acceleration for equation of motion
    dv = a*dt; v += dv # get small changes in v and add to v
    dy = v*dt; y += dy # get small changes in y and add to y

    if v <= 0: # downward motion so drag is upward
        ad *= 1
    if v > 0: # upward motion so drag is downward
        ad *= -1
    if y <= 0: # once the ball hits the ground, the ball will move upwards
               # with a velocity either the same or smaller
        v *= -loss # depends on type of collision
        bounce += 1 # when the ball hits the ground, thats a bounce
        if bounce >= 0 and bounce < num:
            ball.shapesize(2,0.5) # want to make the ball go splat
    
    ball.goto(x, y)
    t += dt
    ball.shapesize(1,1) # shape size should only change when the ball hits the ground
    
    ylist += [y]
    tlist += [t]
    
## plots ##
# get axes
tmin = float(min(tlist)) - 0.1
tmax = float(max(tlist)) + 0.1
ymin = float(min(ylist)) - 1
ymax = float(max(ylist)) + 1
# make figure
plt.figure()
plt.title(f'Change in Height due to Gravity and Drag\nfor an {conservation:s} collision (Mass = {m:,.1f} kg)') 
plt.ylabel('Height (m)')
plt.xlabel('Time (s)')
plt.axis([tmin,tmax,ymin,ymax])
plt.plot(tlist, ylist, 'o', markersize = 1, color = 'blue')

## end program ##
# want to end the program by clicking the screen
turtle.exitonclick()
turtle.bye()