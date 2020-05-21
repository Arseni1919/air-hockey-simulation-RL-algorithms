'''
The class of our agent aka Robot
'''
import Sarsa
import Qlearn
import vars
import Functions
import csv


class Agent():
    # here the user can choose between SARSA and Q-learning
    def __init__(self):
        # ------------------------------------SARSA vs Q-learning------------------------------------#
        # self.ai = Sarsa.Sarsa(
        #     actions=range(vars.num_of_actions),
        #     epsilon=vars.epsilon,
        #     alpha=vars.alpha,
        #     gamma=vars.gamma
        # )
        self.ai = Qlearn.QLearn(
            actions=range(vars.num_of_actions),
            epsilon=vars.epsilon,
            alpha=vars.alpha,
            gamma=vars.gamma
        )
        # ------------------------------------------------------------------------------------------#
        self.lastAction = None
        self.score = 0

    # here actual learning
    def update(self):
        # ------------calculations for graph------
        if self.lastAction is not None:
            vars.for_graph_rob_pos = self.lastState[4]
            vars.for_graph_action = self.lastAction
        # ----------------------------------------
        reward = self.calcReward()
        state = self.calcState()
        vars.action = self.ai.chooseAction(state)
        # print(vars.action)
        if self.lastAction is not None:
            # ------------------------------------SARSA vs Q-learning------------------------------------#
            # self.ai.learn(
            #     self.lastState, self.lastAction, reward, state, vars.action)
            self.ai.learn(
                self.lastState, self.lastAction, reward, state)
            # -------------------------------------------------------------------------------------------#
        self.lastState = state
        self.lastAction = vars.action
        vars.curr_reward = reward
        if reward == vars.hit or reward == vars.miss:
            self.lastAction = None
            vars.episode_in_run = False
        else:
            #print(vars.rob, vars.action)
            Functions.goInDirection(vars.action)


    # Ball tracker:
    def calcState(self):
        return Functions.calc_state_x(), \
               Functions.calc_state_y(),\
               Functions.calc_state_vel(), \
               Functions.calc_state_angle(), \
               Functions.calc_state_rob()

    def calcReward(self):
        # position from simulator
        if vars.x[0] > 24.5:
            return vars.neutral
        vars.episode_in_run = False
        if (vars.rob, self.lastAction, Functions.calc_state_y()) in vars.pos_dict:
            return vars.hit
        return vars.miss

    # for checks
    def print_q_table(self):
        Functions.print_q_table(self.ai.q)

    # writing into csv file
    def write_to_file(self):
        with open('Pxxx.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(vars.first_row)

            states = []
            for key, value in self.ai.q.items():
                if key[0] not in states: states.append(key[0])

            for state in states:
                row = [None, None, None, None, None, None, None, None, None, None, None]
                i = 0
                for s in state:
                    row[i] = s
                    i += 1

                for j in range(6):
                    row[i] = self.ai.q.get((state, j))
                    i += 1

                writer.writerow(row)






