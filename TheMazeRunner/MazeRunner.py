import Environment
import threading
import time
import math 
import random

#initialize discount factor
discountFactor= 0.3

#valid action taken by agent ("up", "down", "left", "right")
actions = Environment.actions

states = []


#make Q table
Q = {}

#make all the state in maze of(19*19)
for i in range(Environment.x):
    for j in range(Environment.y):
        states.append((i, j))


#initialize the Q value of every state to action 
for state in states:
    temp = {}
    for action in actions:
        temp[action] = 0.1
    Q[state] = temp


# initialize the Q value of final state
for action in actions:
    Q[(1,1)][action] = 10


#agent do action and move to next state from current state and receive score form envirnonment and return which action is performed
def do_action(action,learn):
    s = Environment.agent
    r = -Environment.score
    if action == actions[0]:
        Environment.move(0, -1,learn)
    elif action == actions[1]:
        Environment.move(0, 1,learn)
    elif action == actions[2]:
        Environment.move(-1, 0,learn)
    elif action == actions[3]:
        Environment.move(1, 0,learn)
    else:
        return
    s2 = Environment.agent
    r += Environment.score
    return s, action, r, s2


# fetching the maximum value of action with respect to state in Q table
def max_Q(s):
    value = None
    action = None
    for i, j in Q[s].items():
        if value is None or (j > value):
            value = j
            action = i
    return action, value



# after receiving the reward, update the Q table by bellman equation
def UpdateQ(s, a, alpha, reward):
    Q[s][a] =Q[s][a]*( 1 - alpha ) +  (alpha * reward)



# main function
def run():
    global discountFactor
    time.sleep(1)
    alpha = 1
    t = 1
    learn=False

    # run untill agent find the optimal path
    while True:

    	# chaeck the agent is in learning phase or not
    	# if not in learning phase then choose random actions
        if(learn==False):
            print("Without Learning Phase")
            for i in range(0,10000):
                do_action(random.choice(actions),False)
            learn=True


        # write the Q table in Qtable.txt file
        file = open("Qtable.txt",'w')
        file.write("***************************************************************\n")
        for state in states:
            for action in actions:
                file.write(str(Q[state][action])+" ")
            file.write("\n")
        file.write("***************************************************************\n")
        file.close()



        # get the max value from the Q table and perform action
        s = Environment.agent
        max_act, max_val = max_Q(s)
        (state, action, reward, new_state) = do_action(max_act,True)

        max_act, max_val = max_Q(new_state)
        UpdateQ(state, action, alpha, reward + discountFactor* max_val)

        t = t+  1.0
        # check if agent is restart or not
        if Environment.has_restarted():
            Environment.restart_game()
            time.sleep(0.01)
            t = 1.0
        
        alpha =pow(t,-0.1)


        # with for some time , change this value to make maze move slow or fast
        time.sleep(0.001)


t = threading.Thread(target=run)
t.daemon = True
t.start()
Environment.start_game()
