from queue import PriorityQueue
import networkx as nx
import stuff
import matplotlib.pyplot as plt
from utils import heuristic, nodeState,backTracking,getAtenas


G=getAtenas() # Get the Godamm MAP

start="Attiki"
end="Akropoli"

visitedList=[] # Nodes we alredy looked into 
toVisit=PriorityQueue() # The Nodes to visit: get will return de min of all (f(n),count,node)

final=None
found=False
count=0
currentLine=0
lessChanges=True # Opcion para decir si queremos menos trasbordos posibles, google maps implementa algo similar

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



        children=[i for i in G.neighbors(lowestVertex.node)] # All the children of the LowestVertex
        for child in children: # Iterate through all children
            count+=1
            '''
            f(n)=g(n)+h(n)
                g(n): Distance between Parent & Child --> Stored in the Edge of the graph ++ Change of trains
                h(n): How far are we from the end Node --> Need a function to calculate
            '''
            g=lowestVertex.distance+G.edges[(lowestVertex.node,child)]["g(n)"]
            f= g + heuristic() #Calculate f(n)=g(n)+h(n)


            if(lessChanges and currentLine not in G.nodes[child]["lineas"]): #Change of metro line
                f+=6.666



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
color_map=['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'green', 'green', 'red', 'red', 'blue', 'green', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'green', 'green', 'green', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
fig = nx.draw_kamada_kawai(G,with_labels=True,edge_color=color_map,node_size=75,width=6,font_size=7)



plt.legend(["Estaciones"])

#plt.savefig("LineasMetro.png",dpi=2000)
plt.show()
plt.savefig("LineasMetro.png",dpi=2000)
'''
https://www.metrolinemap.com/station/athens/koropi/
Proyecto realizado por: 
#####################################################################################
#                                                                                    # 
#                            ,.--------._                                            #
#                           /            ''.                                         #
#                         ,'                \     |"\                /\          /\  #
#                /"|     /                   \    |__"              ( \\        // ) #
#               "_"|    /           z#####z   \  //                  \ \\      // /  #
#                 \\  #####        ##------".  \//                    \_\\||||//_/   #
#                  \\/-----\     /          ".  \                      \/ _  _ \     #
#                   \|      \   |   ,,--..       \                    \/|(O)(O)|     #
#                   | ,.--._ \  (  | ##   \)      \                  \/ |      |     #
#                   |(  ##  )/   \ `-....-//       |///////////////_\/  \      /     #
#                     '--'."      \                \              //     |____|      #
#                  /'    /         ) --.            \            ||     /      \     #
#               ,..|     \.________/    `-..         \   \       \|     \ 0  0 /     #
#            _,##/ |   ,/   /   \           \         \   \       U    / \_//_/      #
#          :###.-  |  ,/   /     \        /' ""\      .\        (     /              #
#         /####|   |   (.___________,---',/    |       |\=._____|  |_/               #
#        /#####|   |     \__|__|__|__|_,/             |####\    |  ||                #
#       /######\   \      \__________/                /#####|   \  ||                #
#      /|#######`. `\                                /#######\   | ||                #
#     /++\#########\  \                      _,'    _/#########\ | ||                #
#    /++++|#########|  \      .---..       ,/      ,'##########.\|_||                #
#   //++++|#########\.  \.              ,-/      ,'########,+++++\\_\\               #
#  /++++++|##########\.   '._        _,/       ,'######,''++++++++\                  #
# |+++++++|###########|       -----."        _'#######' +++++++++++\                 #
# |+++++++|############\.     \\     //      /#######/++++ +++++ +++\                #
#      ________________________\\___//______________________________________         #
#     / ____________________________________________________________________)        #
#    / /              _                                             _                #
#    | |             | |                                           | |               #
#     \ \            | | _           ____           ____           | |  _            #
#      \ \           | || \         / ___)         / _  )          | | / )           #
#  _____) )          | | | |        | |           (  __ /          | |< (            #
# (______/           |_| |_|        |_|            \_____)         |_| \_)           #
#                                                                                    #
######################################################################################
'''