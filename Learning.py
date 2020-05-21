'''
The main class of LEARNING
הערות:
כשמריצים את הקובץ קופצת תמונה של מגרש עם כדור, חץ שמראה כיוון התקדמות ועיגול שמראה מיקום של רובוט.
מתקדמים בהרצאה פשוט על ידי סגירה (!) של חלונות שיופיעו שוב ושוב עד שמגיעים לגרף עם תוצאות.
אם אתם רוצים להוריד את ההדפסה של מגרש:
ניתן לעשות זאת על ידי מחיקה של שורות קוד רלוונטיים - מוסבר איזה מהם בדיוק בהמשך - למטה
'''
import vars
import Functions
import Agent
from random import randint
import random
import math
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

def start_episode():
    vars.y[0] = randint(vars.min_start_y, vars.max_start_y)
    vars.x[0] = vars.start_x
    vars.vel = random.uniform(vars.min_speed, vars.max_speed)
    vars.angle = random.uniform(vars.min_angle, vars.max_angle)
    vars.rob = 1

def position():
    # start from the
    if vars.x[0] > 24:
        if vars.y[0] <= 0 or vars.y[0] >= 90: vars.angle = 180 - vars.angle

        # velocity change
        vars.vel -= vars.friction
        if vars.vel < 0:
            vars.episode_in_run = False
        else:
            vars.x[0] -= math.sin(math.radians(vars.angle)) * vars.vel
            vars.y[0] += math.cos(math.radians(vars.angle)) * vars.vel

    return vars.x, vars.y


if __name__ == '__main__':
    Functions.prepare()
    # loop for changing parameters. 1 - if we do not need to check another ones
    for parameter in range(1): #[x / 100.0 for x in range(3, 7, 1)]
        print(parameter)

        # how many runs of learning per each point in graph
        # we used 5 or 10 interchangeably:
        for sivuv in range(1): # vars.runs_per_point
            print(' sivuv %s' % sivuv)
            vars.hits = 0
            agent = Agent.Agent()

            # how many episodes we want in each run
            # we used 100 thousands:
            for i in range(vars.episodes):
                vars.episode_in_run = True
                start_episode()
                agent.update()
                while vars.episode_in_run:

                    # amount of frames between updates
                    for j in range(25):
                        position()
                    agent.update()  # error while going up in rob = 2 or down in rob = 0

                    # ---------------------------show field---------------------------#
                    # COMMENT IT OUT IN ORDER TO GET GRAPH DIRECTLY!!!
                    if i % vars.print_every_i_episode == 0:
                        Functions.get_graph(i)
                    # ----------------------------------------------------------------#

                Functions.add_point(i, sivuv)

        # printing q table in console:
        agent.print_q_table()

        # creating csv file:
        agent.write_to_file()

    # showing beautiful graph to presentation
    Functions.hits_point_graph()






# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------




