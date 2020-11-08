from queue import PriorityQueue
from utils import getAtenas
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import neighbors

G=getAtenas()




color_map=["black" for i in G.edges]

n=0
for i in G.edges:
    if(n<60):
        color_map[n]="blue"
    if(n<48):
        color_map[n]="green"
    if(n in [15,14,19,18,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44]):
        color_map[n]="red"
    if(n in [20,22,23,24,25,26,27,28,35]):
        color_map[n]="blue"
    n+=1


print(color_map)

nx.draw_kamada_kawai(G,with_labels=True,edge_color=color_map,node_size=300,width=7,font_size=9)
#nx.draw_networkx(G,with_labels=True,edge_color=color_map[::-1],node_size=300,width=5)
plt.legend(["Estaciones"])
plt.show()