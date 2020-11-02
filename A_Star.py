from queue import PriorityQueue
import networkx as nx
import stuff
import matplotlib.pyplot as plt


class nodeState(): # We can store the path with object refernces
    def __init__(self,node,parent,distance):
        self.node=node
        self.parent=parent
        self.distance=distance

def backTracking(final:nodeState): # We go back from final to start node
    path=[]
    cost=final.distance
    statusNode=final
    
    while(statusNode.parent!=None):
        path.append(statusNode.node)
        statusNode=statusNode.parent
    path.append(statusNode.node)
    return path,cost


G=stuff.getAtenas() # Get the Godamm MAP

start="Attiki"
end="Akropoli"

visitedList=[] # Nodes we alredy looked into 
toVisit=PriorityQueue() # The Nodes to visit: get will return de min of all (f(n),node)

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
            f=lowestVertex.distance+G.edges[(lowestVertex.node,child)]["g(n)"] #Calculate f(n)=g(n)+h(n)
            toInsert=nodeState(child,lowestVertex,f) # Create the tuple (Node,Parent)

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
nx.draw_kamada_kawai(G,with_labels=True,edge_color=color_map,node_size=300,width=7,font_size=9)
plt.legend(["Estaciones"])
plt.show()