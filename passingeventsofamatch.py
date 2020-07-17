def sum(list):
    res = 0
    for i in list[1:]:
        res += i
    return res

import csv
with open("passingevents.csv") as f:
    lis = [line.split() for line in f]        # create a list of lists
    m = input("MatchID to analyze: ")
    t1 = "Huskies"
    t2 = ""
    playersSet = set()
    opponentsSet = set()
    for i, x in enumerate(lis):              #print the list items 
        # x[1] = x[1].split(',')
        x[0] = x[0].split(',')
        t2 = x[0][1]
        if x[0][0] == m:
            if x[0][1] == t1:
                playersSet.add(x[0][2])
                playersSet.add(x[0][3])
            else:
                opponentsSet.add(x[0][2])
                opponentsSet.add(x[0][3])
    playersList = list(playersSet)
    opponentsList = list(opponentsSet)
    playersList.sort()
    opponentsList.sort()
    resP = {key: [0] * 14 for key in playersList}
    resO = {key: [0] * 14 for key in opponentsList}
    for i, x in enumerate(lis):              #print the list items 
        # x[1] = x[1].split(',')
        if x[0][0] == m:
            
            if x[0][1] == t1:
                resP[x[0][2]][playersList.index(x[0][3])] += 1
            else:
                resO[x[0][2]][opponentsList.index(x[0][3])] += 1
    # playersList.insert(0, "Origin player")
    # playersList.append("Total passes: ")
    # opponentsList.insert(0, "Origin player")
    # opponentsList.append("Total passes: ")
# with open("Statistics{}_{}.csv".format(m, t1), mode = 'w') as d1:
#     header_writer1 = csv.writer(d1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     header_writer1.writerow(playersList)
#     stat_writer1 = csv.writer(d1, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for k,v in resP.items():
#         v.insert(0, k)
#         v.append(sum(v))
#         stat_writer1.writerow(v)

# with open("Statistics{}_{}.csv".format(m, t2), mode = 'w') as d2:
#     header_writer2 = csv.writer(d2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     header_writer2.writerow(opponentsList)
#     stat_writer2 = csv.writer(d2, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for k,v in resO.items():
#         v.insert(0, k)
#         v.append(sum(v))
#         stat_writer2.writerow(v)
    
# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# with open("Statistics{}_{}.csv".format(m, t2), 'w') as d2:
#     json.dump(resP, d2)

for k,v in resP.items():
    v.append(sum(v))
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
G = nx.MultiDiGraph()
G.add_nodes_from(playersList)

# G = nx.generators.directed.random_k_out_graph(30, 60, .1)



for originPlayer in playersList:
    for i in range(len(playersList)):
        destPlayer = playersList[i]
        w = resP[originPlayer][i]
        if originPlayer != destPlayer:
            
            # edge_label['{},{}'.format(originPlayer, destPlayer)] = w
            # print(edge_label)
            G.add_edge(originPlayer, destPlayer, weight = w)
edge_label = dict([((u, v), d['weight']) 
                   for u, v, d in G.edges(data=True)])
print(edge_label)

M = G.number_of_edges()
print(M)
node_sizes = 300
edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
elarge = [(u,v) for (u,v,d) in G.edges(data=True) if int(d['weight']) > 7]
eok = [(u,v) for (u,v,d) in G.edges(data=True) if int(d['weight']) > 3 and int(d['weight']) <= 7] # solid edge
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if int(d['weight']) <= 3] # dashed edge
pos = nx.layout.shell_layout(G)
nodes = nx.draw(G,pos,width=1,linewidths=1,\
node_size=node_sizes,node_color='red',alpha=0.9,\
labels={node:node for node in G.nodes()})
nx.draw_networkx_edges(G,pos,edgelist=elarge, arrows="->", width=6, edge_color='m', style='wedged')
nx.draw_networkx_edges(G,pos,edgelist=elarge, arrows="->", width=4, edge_color='g', style='dashed')
nx.draw_networkx_edges(G,pos,edgelist=esmall, arrows="->", width=2,
                       alpha=0.5,edge_color='b')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_label, label_pos=0.8, font_color = 'red')
                               
# set alpha value for each edge
# for i in range(M):
#     edges[i].set_alpha(edge_alphas[i])

# pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Blues)
# pc.set_array(edge_colors)
# plt.colorbar(pc)

ax = plt.gca()
ax.set_axis_off()

plt.show()