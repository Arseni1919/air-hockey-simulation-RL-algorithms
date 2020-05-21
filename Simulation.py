'''
Simulation class
Representation of the physical model of field
Created in purpose to try to 'feel' what simulation does behind the scenes

In order to check the algorithms go to 'Learning' file
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.collections as collections
import vars
from datetime import datetime
from random import randint
import random
import math
import Functions
import csv

def start_episode():
    vars.y[0] = randint(vars.min_start_y, vars.max_start_y)
    vars.x[0] = vars.start_x
    vars.vel = random.uniform(vars.min_speed, vars.max_speed)
    vars.angle = random.uniform(vars.min_angle, vars.max_angle)

def position():

    # start from the
    if vars.x[0] < 0:
        start_episode()

    if vars.y[0] <= 0 or vars.y[0] >= 90: vars.angle = 180 - vars.angle

    # velocity change
    vars.vel -= vars.friction
    if vars.vel < 0:
        vars.x[0] = -1
        vars.y[0] = -1
    else:
        vars.x[0] -= math.sin(math.radians(vars.angle)) * vars.vel
        vars.y[0] += math.cos(math.radians(vars.angle)) * vars.vel
    # print("vel : %s" % vars.vel)
    return vars.x, vars.y

def every_second():
    global ax, c1
    vars.counter += 1
    if vars.counter == 40:
        vars.counter = 0



# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,



# animation function.  This is called sequentially
def animate(i):

    # time counting:

    # global t1
    #
    # t2 = datetime.now()
    # if t2.second - t1.second >= 1:
    #     print('cumulative %s in %s second' % (i, t2.second - t1.second))
    #     t1 = datetime.now()

    # position returns a tuple
    line.set_data(position())
    every_second()
    return line,





if __name__ == '__main__':
    # 147 X 90
    fig = plt.figure('Ball', [7.35, 4.5])
    ax = plt.axes(xlim=(0, 147), ylim=(90, 0))
    line, = ax.plot([], [], 'ro')
    plt.xticks(np.arange(0, 148, 24.5))
    plt.grid(True)


    # vars.q_table = Functions.read_q_file('Pxxx.csv')
    # Functions.print_q_table(vars.q_table)

    t1 = datetime.now()
    start_episode()
    ani = animation.FuncAnimation(fig,
                                  animate,
                                  frames=100,
                                  interval=40,  # 40 - 25 frames per second
                                  blit=True)

    plt.show()