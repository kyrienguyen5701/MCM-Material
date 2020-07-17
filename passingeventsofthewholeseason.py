def sum(list):
    res = 0
    for i in list[1:]:
        res += i
    return res

import csv
with open("passingevents.csv") as f:
    lis = [line.split() for line in f]        # create a list of list
    team = "Huskies"
    playersSet = set()
 
    for i, x in enumerate(lis):              #print the list items 
        # x[1] = x[1].split(',')
        x[0] = x[0].split(',')
        if x[0][1] == team:
            playersSet.add(x[0][2])
    playersList = list(playersSet)
    
    playersList.sort()
    resP = {key: [0] * 30 for key in playersList}
    for i, x in enumerate(lis):              #print the list items 
        # x[1] = x[1].split(',')

        
        if x[0][1] == team:
            resP[x[0][2]][playersList.index(x[0][3])] += 1
#     playersList.insert(0, "Origin player")
#     playersList.append("Total passes ")
# with open("StatisticsOverall_Huskies.csv", mode = 'w') as d:
#     header_writer = csv.writer(d, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     header_writer.writerow(playersList)
#     stat_writer = csv.writer(d, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for k,v in resP.items():
#         v.insert(0, k)
#         v.append(sum(v))
#         stat_writer.writerow(v)
for k,v in resP.items():
    v.append(sum(v))
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

t = 30
G = nx.MultiDiGraph()
G.add_nodes_from(playersList[:t])


for originPlayer in playersList[:t]:
    for i in range(len(playersList[:t])):
        destPlayer = playersList[i]
        w = resP[originPlayer][i]
        if originPlayer != destPlayer and w >= 0:
            
            # edge_label['{},{}'.format(originPlayer, destPlayer)] = w
            # print(edge_label)
            G.add_edge(originPlayer, destPlayer, weight = w)
edge_label = dict([((u, v), d['weight']) 
                   for u, v, d in G.edges(data=True)])


M = G.number_of_edges()
print(M)
node_sizes = 300

edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
elarge = [(u,v) for (u,v,d) in G.edges(data=True) if int(d['weight']) > 90]
eok = [(u,v) for (u,v,d) in G.edges(data=True) if int(d['weight']) > 65 and int(d['weight']) <= 90] # solid edge
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if int(d['weight']) <= 65] # dashed edge
pos = nx.layout.circular_layout(G)
nodes = nx.draw(G,pos,width=1,linewidths=1,\
node_size=node_sizes,node_color='red',alpha=0.9,\
labels={node:node for node in G.nodes()})
nx.draw_networkx_edges(G,pos,edgelist=elarge, arrows="->", width=6, edge_color='m', style='wedged')
nx.draw_networkx_edges(G,pos,edgelist=elarge, arrows="->", width=4, edge_color='g', style='dashed')
nx.draw_networkx_edges(G,pos,edgelist=esmall, arrows="->", width=2,
                       alpha=0.5,edge_color='b')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_label, label_pos=0.75, font_color = 'red')
                               
# set alpha value for each edge
# for i in range(M):
#     edges[i].set_alpha(edge_alphas[i])

# pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Blues)
# pc.set_array(edge_colors)
# plt.colorbar(pc)
textstr = "Number of edges: {}".format(M)


ax = plt.gca()
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
triad_trends = ''
triad_stat = nx.triadic_census(G)
for k, v in triad_stat.items():
    triad_trends += k + ": " + str(v) +"\n"
ax.text(0, 0.85, triad_trends, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
# inn = nx.in_degree_centrality(G)
# out = nx.out_degree_centrality(G)
# with open('centrality.csv', mode = 'w') as cen:
#     header_writer = csv.writer(cen, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     header_writer.writerow(['', 'In-degree-centrality', 'Out-degree-centrality'])
#     stat_writer = csv.writer(cen, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for k in inn:
#         stat_writer.writerow([k, inn[k], out[k]])
ax.set_axis_off()
plt.show()


