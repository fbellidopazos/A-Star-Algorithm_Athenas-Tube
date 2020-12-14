from utils import *
from A_Star import AStar
from difflib import get_close_matches # Nos permite encontrar la palabra mas cercana a una lista de palabras --> Atenas muy raro en nombres...
import matplotlib.pyplot as plt

G=getAtenas() # Get the Godamm MAP

torurist=["Larissa Sta","Panourmo"]
result=[]

nodes=G.nodes
if(len(torurist)>=2):
    if(len(torurist)>2):
        
        for i in range(len(torurist)-1):
            
            start=get_close_matches(torurist[i],nodes,1)[0] 
            end=get_close_matches(torurist[i+1],nodes,1)[0]

            path=AStar(G,start,end)[0]
            
            result.extend(path)
            showMapFull(G,path,"magenta")
        print("Todas las estaciones visitadas")
        print("================================================")
        showMapFull(G,result,"magenta")



    if(len(torurist)==2):
        start=get_close_matches(torurist[0],nodes,1)[0]
        end=get_close_matches(torurist[1],nodes,1)[0]

        path,searchPath=AStar(G,start,end)
        showMapFull(G,searchPath,"magenta")
        showMapFull(G,path,"Lime")
    
else:
    print("You lazy person, give me destinations")
    
'''
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
Proyecto realizado por: 
• Enrique Santatecla
• Ivan Tello Lopez
• Santiago Moreno Dominguez
• Pablo San Miguel Martín
• Jaime Gonzalez Delgado
• Fernando Bellido Pazos
'''