from queue import PriorityQueue
import networkx as nx
import stuff
import matplotlib.pyplot as plt
from utils import nodeState,backTracking,getAtenas







G=getAtenas() # Get the Godamm MAP

start="Attiki"
end="Akropoli"

visitedList=[] # Nodes we alredy looked into 
toVisit=PriorityQueue() # The Nodes to visit: get will return de min of all (f(n),count,node)

final=None
found=False
count=0

toVisit.put((0,0,nodeState(start,None,0))) # Obvious but add the start to toVisit 

while(not toVisit.empty() and (not found)): # We have nodes to visit 
    lowest=toVisit.get() # Lowest value of f(n) from priority Queue
    lowestVertex=lowest[2] # Get the node with f(n) lowest nodeState(node,parent)

    visitedList.append(lowestVertex.node) # We visit the node, add it to the list
    
    
    if(lowestVertex.node==end):
        found=True # Yeay we have found it, lets stop 
        final=lowestVertex # Save the node for backtracking
    else:
        children=[i for i in G.neighbors(lowestVertex.node)] # All the children of the LowestVertex
        for child in children: # Iterate through all children
            count+=1
            '''
            f(n)=g(n)+h(n)
                g(n): Distance between Parent & Child --> Stored in the Edge of the graph
                h(n): How far are we from the end Node --> Need a function to calculate
            '''
            g=lowestVertex.distance+G.edges[(lowestVertex.node,child)]["g(n)"]
            f= g #Calculate f(n)=g(n)+h(n)
            toInsert=nodeState(child,lowestVertex,g) # Create the tuple (Node,Parent,cost2getHere)

            if(toInsert.node not in visitedList): # Check if we have alredy been there (NO endless Loops)
                toVisit.put((f,count,toInsert)) # We will need further examination of the node
                


        

if(found): # Congrats we have found something
    path,cost=backTracking(final)
    print(path)
    print(cost)
else: # Something smells like a Bug in the Code..... Or the really Intelligent USER 
    print("No path could be found. ¯\_(ツ)_/¯ ")

# Show the Map
color_map=['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'green', 'green', 'red', 'red', 'green', 'blue', 'blue', 'green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
fig = nx.draw_kamada_kawai(G,with_labels=True,edge_color=color_map,node_size=75,width=6,font_size=5)


plt.legend(["Estaciones"])

plt.savefig("LineasMetro.png",dpi=1800)
plt.show()

