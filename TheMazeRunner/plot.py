import matplotlib.pyplot as plt
import csv


# plot for agent when not in learning phase 
# agent takes random actions
# open the file ScoreWithoutLearn.txt and takes the data as input 
x=[]
y=[]

with open('ScoreWithoutLearn.txt','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=' ')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y,label='loaded from ScoreWithoutLearn')

plt.xlabel("Number of steps")
plt.ylabel("Score")
plt.legend()
plt.show()




# plot the graph when agent is in learning phase
# agent take action according to Q learning
# open the file ScoreWithLearn.txt and takes the data as input
x=[]
y=[]

with open('ScoreWithLearn.txt','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=' ')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y,label='loaded from ScoreWithLearn')

plt.xlabel("Number of Runs")
plt.ylabel("Score")
plt.legend()
plt.show()