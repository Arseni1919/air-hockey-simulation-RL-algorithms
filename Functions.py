'''
File with all supporting functions we need
In most cases the purpose of each function can be understood from its' names
'''

import vars
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import math

# ----------------------------------------------------------------------------------#
# all calculations taking in account the gausian noise to simulate real measurements
# ----------------------------------------------------------------------------------#

def calc_state_x():
    '''
    x:
    0       - 24.5  - 0
    24.5    - 49    - 1
    49      - 73.5  - 2
    73.5    - 98    - 3
    98      - 122.5 - 4
    122.5   - 147   - 5
    '''
    x = np.random.normal(vars.x[0], vars.gausian_cm)
    if x < 0:
        raise Exception()
    if x <= 24.5:
        return 0
    if 24.5 < x <= 49:
        return 1
    if 49 < x <= 73.5:
        return 2
    if 73.5 < x <= 98:
        return 3
    if 98 < x <= 122.5:
        return 4
    if 122.5 < x:
        return 5
    if x > 149:
        raise Exception()

def calc_state_y():
    '''
    y:
    0 - 10  - 0
    10 - 20 - 1
    20 - 30 - 2
    30 - 40 - 3
    40 - 50 - 4
    50 - 60 - 5
    60 - 70 - 6
    70 - 80 - 7
    80 - 90 - 8
    '''
    y = np.random.normal(vars.y[0], vars.gausian_cm)
    if y < -3:
        raise Exception()
    if y <= 10:
        return 0
    if 10 < y <= 20:
        return 1
    if 20 < y <= 30:
        return 2
    if 30 < y <= 40:
        return 3
    if 40 < y <= 50:
        return 4
    if 50 < y <= 60:
        return 5
    if 60 < y <= 70:
        return 6
    if 70 < y <= 80:
        return 7
    if 80 < y:
        return 8
    if y > 95:
        raise Exception()

def calc_state_vel():
    '''
    Amplitude ( 0-20    - 0,
                20-40   - 1,
                40-60   - 2,
                60<*    - 3
                )
    '''
    vel = np.random.normal(vars.vel, vars.gausian_cm_s)
    if  vel <= 0.8:
        return 0
    if 0.8 < vel <= 1.6:
        return 1
    if 1.6 < vel <= 2.4:
        return 2
    if 2.4 < vel:
        return 3

def calc_state_angle():
    '''
    Angle ( 0-45    - 0,
            45-90   - 1,
            90-135  - 2,
            135-180 - 3,
            180-225 - 4,
            225-270 - 5,
            270-315 - 6,
            315-360 - 7
            )
    '''
    ang = np.random.normal(270 - vars.angle, vars.gausian_angle)
    if ang <= 45:
        return 0
    if 45 < ang <= 90:
        return 1
    if 90 < ang <= 135:
        return 2
    if 135 < ang <= 180:
        return 3
    if 180 < ang <= 225:
        return 4
    if 225 < ang <= 270:
        return 5
    if 270 < ang <= 315:
        return 6
    if 315 < ang:
        return 7

def calc_state_rob():
    '''
    upper   - 0
    middle  - 1
    bottom  - 2
    '''
    return vars.rob

# changes the state of robot
def goInDirection(action):
    if action == vars.Md and vars.rob == 0:
        raise Exception('action == Md and vars.rob == 0')
    if action == vars.Mu and vars.rob == 2:
        raise Exception('action == Mu and vars.rob == 2')
    if action == vars.Mu: vars.rob += 1
    if action == vars.Md: vars.rob -= 1
    if vars.rob > 2 or vars.rob < 0:
        raise Exception('vars.rob > 2 or vars.rob < 0')

def array_of_actions():
    if vars.rob == 0:
        return [vars.Mu, vars.N, vars.Ku, vars.Kc, vars.Kd]
    if vars.rob == 2:
        return [vars.Md, vars.N, vars.Ku, vars.Kc, vars.Kd]
    return [vars.Mu, vars.Md, vars.N, vars.Ku, vars.Kc, vars.Kd]

# other help functions to print, read and write to files and so on:

def print_q_table(q):
    states = []
    for key, value in q.items():
        if key[0] not in states: states.append(key[0])
        # print(key[0])
        # print(key[1])

    for state in states:
        for s in state:
            if s is None:
                raise Exception('state is None')
            print('%s - \t' % s, end='')
        #print(state)

        for i in range(6):  # state - action
            print(q.get((state, i)), end=' ')
        print()

def read_q_file(str):
    q = {}
    #q[(state, action)] = reward
    # ['x','y','amplitude','angle','rob','action 0','action 1', 'action 2', 'action 3', 'action 4', 'action 5']
    with open(str, mode='r') as csv_file:
        print("read Pxxx.csv")
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for i in range(6):
                try:
                    q[((int(row['x']), int(row['y']), int(row['amplitude']), int(row['angle']), int(row['rob'])),
                        i)] = float(row['action %s' % i])
                except ValueError:
                    #print(row['!!!!!!!!!!!!!!!!!!!!!action %s' % i])
                    continue
    return q

def get_graph(i):
    fig = plt.figure('Iteration: %s, Robot: %s, Result: %s' % (i,vars.rob_dict[vars.rob],vars.curr_reward), [7.35, 4.5])
    ax = plt.axes(xlim=(0, 147), ylim=(90, 0))
    line, = ax.plot([], [], 'ro')
    plt.xticks(np.arange(0, 148, 24.5))
    plt.grid(True)
    line.set_data(vars.x, vars.y)
    plt.scatter(get_coordinates_of('x'), get_coordinates_of('y'), c='c', s=700, alpha=0.3) # for robot
    #ax.text(34.5, 45, "All rights reserved to Arseni The Russian Boy", dict(size=10, color='gray'))
    ax.annotate('',
                xy=(vars.x[0] - 10 * math.sin(math.radians(vars.angle)), vars.y[0] + 10 * math.cos(math.radians(vars.angle))),
                xytext=(vars.x[0], vars.y[0]),
                arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()

def get_coordinates_of(part):
    if part == 'x':
        vars.rob_state_dict.get((vars.for_graph_rob_pos, vars.for_graph_action), Exception())
        return vars.rob_state_dict[vars.for_graph_rob_pos, vars.for_graph_action][0]
    if part == 'y':
        return vars.rob_state_dict[vars.for_graph_rob_pos, vars.for_graph_action][1]

def count_hits(i):
    if vars.curr_reward == vars.hit: vars.hits += 1
    if vars.curr_reward == vars.miss: vars.misses += 1
    if i % 1000 == 0:
        vars.x_hits.append(i)
        vars.y_hits.append(vars.hits)
        #print('hits in iter %s is %s' %(i, vars.hits))
        #print('misses in iter %s is %s' % (i,vars.misses))
        vars.hits = 0
        vars.misses = 0

def hits_graph():
    print(vars.x_hits)
    print(vars.y_hits)
    x = np.array(vars.x_hits)
    y = np.array(vars.y_hits)
    ax = plt.axes()
    #ax.text(34.5, 45, "All rights reserved to Arseni The Russian Boy", dict(size=10, color='gray'))
    plt.plot(x,y)
    plt.plot(x, y, 'ob')
    plt.show()

def prepare():
    vars.x_hits = {}

def add_point(i, sivuv, parameter = -1):
    if parameter == -1:
        # print('here')
        if vars.curr_reward == vars.hit: vars.hits += 1
        if i % vars.dgima == 0:
            if sivuv == 0:
                vars.x_hits[i] = []
            vars.x_hits[i].append(vars.hits)
            vars.hits = 0
    else:
        if vars.curr_reward == vars.hit and i > 89000: vars.hits += 1
        if i == vars.dgima:
            if sivuv == 0:
                vars.x_hits[parameter] = []
            vars.x_hits[parameter].append(vars.hits)
            vars.hits = 0

def hits_point_graph():
    x = []
    y = []
    for key, value in vars.x_hits.items():
        x.append(key)
        y.append(np.average(vars.x_hits[key]))
    x = np.array(x)
    y = np.array(y)

    ax = plt.axes()
    #ax.text(34.5, 45, "All rights reserved to Arseni The Russian Boy", dict(size=10, color='gray'))
    # plt.hist(x,bins=[0,1])
    plt.plot(x,y)
    #plt.plot(x, y, 'or')
    plt.show()

    vars.x_hits = []
