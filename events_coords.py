import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
fig, ax = plt.subplots()
import csv
with open("passingevents.csv") as f:
    lis = [line.split() for line in f]       # create a list of list
    m = input("MatchID to analyze: ")
    player = "Huskies_" + input("Name: ")
    team = "Huskies"
    for i, x in enumerate(lis):
        if len(x) > 1:
            x[0] = x[0].split(',')
            x[1] = x[1].split(',')
        if (x[0][0] == m or m == 0) and x[0][1] == team:
            if x[0][2] == player:
            
                ax.scatter(float(x[1][1]), float(x[1][2]), marker='o', c='r', edgecolor='b')
            if x[0][3] == player:
                ax.scatter(float(x[1][3]), float(x[1][4]), marker='o', c='g', edgecolor='b')

        
# for color in ['tab:blue', 'tab:orange', 'tab:green']:
    
#     x, y = np.random.rand(2, n)
#     scale = 200.0 * np.random.rand(n)
#     ax.scatter(x, y, c=color, s=scale, label=color,
#                alpha=0.3, edgecolors='none')

ax.legend()
axes = plt.gca()
axes.set_xlim([0,100])
axes.set_ylim([0,100])

plt.show()