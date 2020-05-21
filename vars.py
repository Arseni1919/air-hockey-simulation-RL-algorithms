'''
Class of all necessary variables of the program
'''
import math

# state


x = [147.0]

y = [45.0]

vel = 1.0

angle = 90

rob = 1
rob_dict = {0: '0-30',
            1: '30-60',
            2: '60-90'}

# action
Mu  = 0
Md  = 1
N   = 2
Ku  = 3
Kc  = 4
Kd  = 5
action_dict = { Mu:'Move up',
                Md:'Move down',
                N:'Do not move',
                Ku:'Kick up',
                Kc:'Kick center',
                Kd:'Kick down'}

action = -1


counter  = 0

min_speed = 1
max_speed = 3
min_angle = 60
max_angle = 120
friction = 0.001

min_start_y = 1
max_start_y = 89
start_x = 147

num_of_actions = 6

hit = 10.0
miss = -10.0
neutral = 0.0

epsilon = 0.04 #0.1
alpha = 0.1 #0.1
gamma = 0.75 #0.9
gausian_cm = 0.01
gausian_cm_s = 0.01
gausian_angle = 0.01

startCell = 0

pos_dict = [
    (0,5,0),
    (0,4,1),
    (0,3,2),
    (1,5,3),
    (1,4,4),
    (1,3,5),
    (2,5,6),
    (2,4,7),
    (2,3,8),
    (0,2,1),
    (1,2,4),
    (2,2,7)
]



first_row = ['x','y','amplitude','angle','rob','action 0','action 1', 'action 2', 'action 3', 'action 4', 'action 5']

q_table = {}

bool_for_second = True

curr_reward = 0.0

hits = 0
misses = 0
stops = 0
x_hits = []
y_hits = []

# vars for graph
for_graph_rob_pos = 0
for_graph_action = 0

episode_in_run = True

episodes = 50001
print_every_i_episode = 50000
runs_per_point = 5
dgima = 1000

# rob - action -> pos x - pos y
rob_state_dict = {}
rob_state_dict[0,0] = 12.25, 45
rob_state_dict[0,2] = 12.25, 15
rob_state_dict[0,3] = 24.5, 25
rob_state_dict[0,4] = 24.5, 15
rob_state_dict[0,5] = 24.5, 5
rob_state_dict[1,0] = 12.25, 75
rob_state_dict[1,1] = 12.25, 15
rob_state_dict[1,2] = 12.25, 45
rob_state_dict[1,3] = 24.5, 55
rob_state_dict[1,4] = 24.5, 45
rob_state_dict[1,5] = 24.5, 35
rob_state_dict[2,1] = 12.25, 45
rob_state_dict[2,2] = 12.25, 75
rob_state_dict[2,3] = 24.5, 85
rob_state_dict[2,4] = 24.5, 75
rob_state_dict[2,5] = 24.5, 65