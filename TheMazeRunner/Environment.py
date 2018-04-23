from tkinter import *
mazemap = Tk()


# set the environment variables of maze like width and initial and final position
# Valid actions ,without_Learning_count, with_learning_count, reward

widthOfMaze = 40
(x, y) = (19, 19)
actions = ["up", "down", "left", "right"]
without_Learning_count=0
with_learning_count=0
finishing_point = [(1, 1)]


# Bulding a Maze board 
board = Canvas(mazemap, width=x*widthOfMaze, height=y*widthOfMaze)
agent = (y-2, y-2)
score = 1
restart = False
normalReward = -0.05


# set the walls
walls = [
        (0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),(0,15),(0,16),(0,17),(0,18),
        (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),
        (0,18),(1,18),(2,18),(3,18),(4,18),(5,18),(6,18),(7,18),(8,18),(9,18),(10,18),(11,18),(12,18),(13,18),(14,18),(15,18),(16,18),(17,18),(18,18),
        (18,0),(18,1),(18,2),(18,3),(18,4),(18,5),(18,6),(18,7),(18,8),(18,9),(18,10),(18,11),(18,12),(18,13),(18,14),(18,15),(18,16),(18,17),(18,18),
        (2,2),(2,3),(2,4),(13,1),(3,2),(4,2),(5,2),(9,2),(13,2),(15,2),(9,3),(13,3),(15,3),(4,4),(5,4),(9,4),(13,4),(15,4),(2,5),(4,5),(9,5),(13,5),(15,5),
        (2,6),(4,6),(5,6),(6,6),(7,6),(8,6),(9,6),(13,6),(14,6),(15,6),(2,7),(9,7),(2,8),(3,8),(4,8),(5,8),(9,8),(13,8),(14,8),(15,8),(17,8),(2,9),(4,9),
        (9,9),(1,10),(2,10),(4,10),(6,10),(9,10),(10,10),(11,10),(12,10),(13,10),(14,10),(15,10),(6,11),(13,11),(15,11),(2,12),(3,12),(4,12),(5,12),(6,12),(6,12),(7,12),(8,12),
        (9,12),(10,12),(11,12),(12,12),(13,12),(15,12),(6,13),(15,13),(1,14),(2,14),(3,14),(4,14),(6,14),(7,14),(8,14),(9,14),(13,14),(14,14),(15,14),(4,15),(2,16),(4,16),(5,16),(6,16)
        ,(9,16),(10,16),(11,16),(12,16),(13,16),(14,16),(15,16),(2,17),(11,1),(11,2),(11,4),(11,5),(11,6),(11,7),(12,4),(17,12)
        ,(7,1),(7,2),(7,3)
        ]



# now creating a maze 
def render_grid():
    global walls, widthOfMaze, x, y, agent

    # creating a white rectangular box in which agent can land
    for i in range(x):
        for j in range(y):
            board.create_rectangle(i*widthOfMaze,
                                   j*widthOfMaze,
                                   (i+1)*widthOfMaze, 
                                   (j+1)*widthOfMaze,
                                   fill="white",
                                   width=1)
    # create the green rectangular box which is destination point for agent        
    board.create_rectangle(widthOfMaze,
                           widthOfMaze,
                           2*widthOfMaze,
                           2*widthOfMaze,
                           fill="green",
                           width=1)

    # creating the walls of black colour
    for (i, j) in walls:
        board.create_rectangle(i*widthOfMaze,
                               j*widthOfMaze,
                               (i+1)*widthOfMaze,
                               (j+1)*widthOfMaze,
                               fill="black",
                               width=1)

render_grid()


# in this function agent move to next state and return the score 
def move(dx, dy,learn):
    global agent, x, y, score, normalReward, ball, restart,without_Learning_count,with_learning_count


    # check if the agent in learning phase or not
    if(learn==True):

        # write the score in ScoreWithLearn.txt file for ploting a graph
        file=open("ScoreWithLearn.txt",'a')
        if restart == True:
            restart_game()
        nextRow = agent[0] + dx
        nextColumn = agent[1] + dy
        score += normalReward
        # check if the agent can move to next step or not
        if (nextRow >= 0) and (nextRow < x) and (nextColumn >= 0) and (nextColumn < y) and not ((nextRow, nextColumn) in walls):
            # change the ball position
            board.coords(ball,
                         nextRow*widthOfMaze+widthOfMaze*2/10,
                         nextColumn*widthOfMaze+widthOfMaze*2/10,
                         nextRow*widthOfMaze+widthOfMaze*8/10,
                         nextColumn*widthOfMaze+widthOfMaze*8/10)
            agent = (nextRow, nextColumn)


        # check if the agent reaches the final point    
        if nextRow == 1 and nextColumn == 1:
            score -= normalReward
            score += 1
            if score > 0:
                with_learning_count+=1
                print("Reached at finishing_point with score: ",score)
                file.write(str(with_learning_count)+" "+str(score)+"\n")
                restart=False
            else:
                with_learning_count+=1
                print("Reached at finishing_point with score: ",score)
                file.write(str(with_learning_count)+" "+str(score)+"\n")
            restart = True
            return

        print ("score: ", score)




    elif(learn==False):
        # write the score in ScoreWithLearn.txt file for ploting a graph
        file=open("ScoreWithoutLearn.txt",'a')
        if restart == True:
            restart_game()
        nextRow = agent[0] + dx
        nextColumn = agent[1] + dy
        score += normalReward
         # check if the agent reaches the final point
        if (nextRow >= 0) and (nextRow < x) and (nextColumn >= 0) and (nextColumn < y) and not ((nextRow, nextColumn) in walls):
            # change the ball position
            board.coords(ball,
                         nextRow*widthOfMaze+widthOfMaze*2/10,
                         nextColumn*widthOfMaze+widthOfMaze*2/10,
                         nextRow*widthOfMaze+widthOfMaze*8/10,
                         nextColumn*widthOfMaze+widthOfMaze*8/10)
            agent = (nextRow, nextColumn)

            
# check if the agent reaches the final point 
        if nextRow == 1 and nextColumn == 1:
            score -= normalReward
            score += 1
            restart = True
            return
        without_Learning_count+=1
        print(str(without_Learning_count),":",str(score))
        file.write(str(without_Learning_count)+" "+str(score)+"\n")
        


def call_up(event):
    move(0, -1)
def call_down(event):
    move(0, 1)
def call_left(event):
    move(-1, 0)
def call_right(event):
    move(1, 0)



# if maze is restart then move the agent to initial position and re run the agent
def restart_game():
    global agent, score, ball, restart
    agent = (y-2, y-2)
    score = 1
    restart = False
    board.coords(ball,
                agent[0]*widthOfMaze+widthOfMaze*2/10,
                agent[1]*widthOfMaze+widthOfMaze*2/10,
                agent[0]*widthOfMaze+widthOfMaze*8/10,
                agent[1]*widthOfMaze+widthOfMaze*8/10)



def has_restarted():
    return restart


mazemap.bind("<Up>", call_up)
mazemap.bind("<Down>", call_down)
mazemap.bind("<Right>", call_right)
mazemap.bind("<Left>", call_left)



# creating a agent which green colour ball
ball = board.create_oval(agent[0]*widthOfMaze+widthOfMaze*2/10,
                         agent[1]*widthOfMaze+widthOfMaze*2/10,
                         agent[0]*widthOfMaze+widthOfMaze*8/10,
                         agent[1]*widthOfMaze+widthOfMaze*8/10,
                         fill="green",
                         width=1,
                         tag="ball")

board.grid(row=0, column=0)


def start_game():
    mazemap.mainloop()
