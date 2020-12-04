from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt
from utils import heuristic, nodeState,backTracking,getAtenas 

def AStar(G,start:str,end:str,lessChanges=True):
    
    visitedList=[] # Nodes we alredy looked into 
    toVisit=PriorityQueue() # The Nodes to visit: get will return de min of all (f(n),count,node)

    final=None
    found=False
    count=0
    currentLine=0
    

    toVisit.put((0,0,nodeState(start,None,0))) # Obvious but add the start to toVisit 

    while(not toVisit.empty() and (not found)): # We have nodes to visit 
        lowest=toVisit.get() # Lowest value of f(n) from priority Queue
        lowestVertex=lowest[2] # Get the node with f(n) lowest nodeState(node,parent)

        visitedList.append(lowestVertex.node) # We visit the node, add it to the list
        
        

        if(lowestVertex.node==end):
            found=True # Yeay we have found it, lets stop 
            final=lowestVertex # Save the node for backtracking
        else:
            '''
            Miramos si hemos cambiado de linea, de ese modo podremos calcular el coste real de pasar a la siguiente parada
            '''
            if(lessChanges and currentLine not in G.nodes[lowestVertex.node]["lineas"]):
                currentLine=G.nodes[lowestVertex.node]["lineas"][0]
                if(start == lowestVertex.node):
                    if(G.nodes[end]["lineas"][0] in G.nodes[lowestVertex.node]["lineas"]):
                        currentLine = currentLine=G.nodes[end]["lineas"][0]
                



            children=[i for i in G.neighbors(lowestVertex.node)] # All the children of the LowestVertex
            for child in children: # Iterate through all children
                count+=1
                '''
                f(n)=g(n)+h(n)
                    g(n): Distance between Parent & Child --> Stored in the Edge of the graph ++ Change of trains
                    h(n): How far are we from the end Node --> Need a function to calculate
                '''
                g=lowestVertex.distance+G.edges[(lowestVertex.node,child)]["g(n)"]
                
                change=False
                if(lessChanges and currentLine not in G.nodes[child]["lineas"]): #Change of metro line
                    g+=6.666 # Se aumenta G ya que el coste para pasar por esa arista es mayor al haber trasbordo
                    change=True # Si hemos cambiado de linea guardarlo para luego buscar en numero de trasbordos 
                
                f= g + heuristic(G,child,end) #Calculate f(n)=g(n)+h(n)


                toInsert=nodeState(child,lowestVertex,g,change) # Create the tuple (Node,Parent,cost2getHere,changeOfTrain)

                if(toInsert.node not in visitedList): # Check if we have alredy been there (NO endless Loops)
                    toVisit.put((f,count,toInsert)) # We will need further examination of the node
    if(found): # Congrats we have found something
        path,cost,changes=backTracking(final)
        print(f'\nPath from {start} to {end}')
        print("===========================================")
        print(f'Path to destiny: {path}')
        print(f'Total kilometers: {cost}')
        print(f'Number of changes: {changes}')
        return path,visitedList
    else: # Something smells like a Bug in the Code..... Or the really Intelligent USER 
        print("No path could be found. ¯\_(ツ)_/¯ ")
        


