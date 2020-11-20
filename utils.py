import networkx as nx
import math
import matplotlib.pyplot as plt

class nodeState(): # We can store the path with object refernces
    def __init__(self,node,parent,distance,change=False):
        self.node=node
        self.parent=parent
        self.distance=distance
        self.change=change

def backTracking(final:nodeState): # We go back from final to start node
    path=[]
    cost=final.distance
    statusNode=final
    changes=0
    while(statusNode.parent!=None):
        path.append(statusNode.node)
        statusNode=statusNode.parent
        if(statusNode.change):
            changes+=1
    path.append(statusNode.node)
    return path,cost,changes

def heuristic(G,nodeFrom,nodeTo):
    (x1,y1) = G.nodes[nodeFrom]["coordenadas"]
    (x2,y2) = G.nodes[nodeTo]["coordenadas"]

    R = 6378137 #metros
    dLat = rad(x2 - x1)
    dLong = rad(y2 - y1)

    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(rad(x1)) * math.cos(rad(x2)) * math.sin(dLong / 2) * math.sin(dLong / 2)

    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    d = R*c

    return d/1000
    #return 0

def rad(x):
    return x*math.pi/180
def colorNodes(G,nodes,color="Yellow"):
    nodeColor=[]
    
    for i in G.nodes:
        

        if(i in nodes):
            nodeColor.append(color)
        else:
            nodeColor.append("lightblue")
    return nodeColor


def showMapFull(G,node2Color=[],color="Yellow"):
    # Show the Map
    color_map=['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'green', 'green', 'red', 'red', 'blue', 'green', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'green', 'green', 'green', 'green', 'green', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']


    fig = nx.draw_kamada_kawai(G,with_labels=True,edge_color=color_map,node_color=colorNodes(G,node2Color,color),node_size=100,width=6,font_size=7)
    


    plt.legend(["Estaciones"])
    
    #plt.savefig("LineasMetro.png",dpi=1200)
    plt.show()
def getAtenas():
    G = nx.Graph()

    Nodos = [
        ("Kifissia",{"lineas":[1],"coordenadas":(38.0736817,23.8083101) }),
        ("KAT",{"lineas":[1], "coordenadas":(38.065833, 23.803889)}),
        ("Maroussi",{"lineas":[1], "coordenadas":(38.0561704,23.804973) }),
        ("Neratziotissa",{"lineas":[1], "coordenadas":(38.0450788,23.7931536) }),
        ("Eirini",{"lineas":[1], "coordenadas":(38.043732,23.782722) }),
        ("Iraklio",{"lineas":[1], "coordenadas":(38.0462534,23.7660751) }),
        ("Nea Ionia",{"lineas":[1], "coordenadas":(38.041612,23.7551964) }),
        ("Pefkakia",{"lineas":[1], "coordenadas":(38.0371452,23.750169) }),
        ("Perissos",{"lineas":[1], "coordenadas":(38.032656,23.7447428) }),
        ("Ano Patisia",{"lineas":[1], "coordenadas":(38.023795,23.735964) }),
        ("Aghios Eleftherios",{"lineas":[1], "coordenadas":(38.0201134,23.7318585) }),
        ("Kato Patisia",{"lineas":[1], "coordenadas":(38.0115762,23.7287924) }),
        ("Aghios Nikolaos",{"lineas":[1], "coordenadas":(38.006919,23.727711) }),
        ("Attiki",{"lineas":[1,2], "coordenadas":(37.9994388,23.7227672) }),
        ("Victoria",{"lineas":[1], "coordenadas":(37.9930768,23.7302859) }),
        ("Omonia",{"lineas":[1,2], "coordenadas":(37.9841465,23.7280893) }),
        ("Monastiraki",{"lineas":[1,3], "coordenadas":(37.9760854,23.7256256) }),
        ("Thissio",{"lineas":[1], "coordenadas":(37.9767093,23.7207061) }),
        ("Petralona",{"lineas":[1], "coordenadas":(37.968624,23.709244) }),
        ("Tavros",{"lineas":[1], "coordenadas":(37.962938,23.703982) }),
        ("Kalithea",{"lineas":[1], "coordenadas":(37.9604041,23.6973321) }),
        ("Moschato",{"lineas":[1], "coordenadas":(37.9550584,23.6797009) }),
        ("Faliro",{"lineas":[1], "coordenadas":(37.9449872,23.6652251) }),
        ("Piraeus",{"lineas":[1], "coordenadas":(37.9481116,23.6432721) }),
        
        ("Anthoupoli",{"lineas":[2], "coordenadas":(38.017128,23.6910971)  }),# Estacion Nueva!
        ("Peristeri",{"lineas":[2], "coordenadas":(38.0131614,23.6955021) }),# Estacion Nueva!
        ("Aghios Antonios",{"lineas":[2], "coordenadas":(38.0066608,23.6994812) }),
        ("Sepolia",{"lineas":[2], "coordenadas":(38.0026462,23.7135386) }),
        ("Larissa Station",{"lineas":[2], "coordenadas":(37.9919943,23.7211021) }),
        ("Metaxourghio",{"lineas":[2], "coordenadas":(37.9862735,23.721142) }),
        ("Panepistimio",{"lineas":[2], "coordenadas":(37.9803868,23.7330517) }),
        ("Syntagma",{"lineas":[2,3], "coordenadas":(37.9750848,23.7356843) }),
        ("Akropoli",{"lineas":[2], "coordenadas":(37.9687331,23.7296004) }),
        ("Sygrou-Fix",{"lineas":[2], "coordenadas":(37.9642909,23.7265661) }),
        ("Neos Kosmos",{"lineas":[2], "coordenadas":(37.9575978,23.7284651) }),
        ("Aghios Ioannis",{"lineas":[2], "coordenadas":(37.9566294,23.7346841) }),
        ("Dafni",{"lineas":[2], "coordenadas":(37.949571,23.737194) }),
        ("Aghios Dimitrios",{"lineas":[2], "coordenadas":(37.9492027,23.7372232) }),
        ("Ilioupoli",{"lineas":[2], "coordenadas":(37.9298108,23.7445277) }),# Estacion Nueva!
        ("Alimos",{"lineas":[2], "coordenadas":(37.918129,23.744583) }),# Estacion Nueva!
        ("Argyroupoli",{"lineas":[2], "coordenadas":(37.903267,23.745377) }),# Estacion Nueva!
        ("Elliniko",{"lineas":[2], "coordenadas":(37.8925685,23.7471345) }),# Estacion Nueva!

        ("Nikaia",{"lineas":[3], "coordenadas":(37.9657103,23.6473525) }),# Estacion Nueva!
        ("Korydallos",{"lineas":[3], "coordenadas":(37.977031,23.6504424) }),# Estacion Nueva!
        ("Agia Varvara",{"lineas":[3], "coordenadas":(37.9972525,23.6673709) }),# Estacion Nueva!
        ("Egaleo",{"lineas":[3], "coordenadas":(37.991956,23.6818295) }), 
        ("Eleonas",{"lineas":[3], "coordenadas":(37.9878939,23.6941771) }),
        ("Kerameikos",{"lineas":[3], "coordenadas":(37.978584,23.711462)}),
        ("Evangelismos",{"lineas":[3], "coordenadas":(37.9771694,23.7465741) }),
        ("Megaro Moussikis",{"lineas":[3], "coordenadas":(37.979287,23.7529123) }),
        ("Ambelokipi",{"lineas":[3], "coordenadas":(37.987325,23.7570287) }),
        ("Panormou",{"lineas":[3], "coordenadas":(37.9931611,23.7634197) }),
        ("Katehaki",{"lineas":[3], "coordenadas":(37.9931675,23.7761521) }),
        ("Ethniki Amyna",{"lineas":[3], "coordenadas":(38.0000539,23.7857518) }),
        ("Holargos",{"lineas":[3], "coordenadas":(38.0045199,23.7947237) }),
        ("Nomismatokopio",{"lineas":[3], "coordenadas":(38.009275,23.8056672) }),
        ("Aghia Paraskevi",{"lineas":[3], "coordenadas":(38.0171912,23.812319) }),
        ("Halandri",{"lineas":[3], "coordenadas":(38.0215145,23.8212267) }),
        ("Doukissis Plakentias",{"lineas":[3], "coordenadas":(38.0245952,23.8342763) }),
        ("Pallini",{"lineas":[3], "coordenadas":(38.0058365,23.8695869) }),
        ("Paiania",{"lineas":[3], "coordenadas":(37.9836442,23.86989) }),
        ("Koropi",{"lineas":[3], "coordenadas":(37.9130084,23.8958108) }),
        ("Airport",{"lineas":[3], "coordenadas":(37.9369208,23.9447987) })
    ]
    G.add_nodes_from(Nodos)

    Aristas=[
        ("Kifissia","KAT",{"g(n)":1,"lineas":1}),
        ("KAT","Maroussi",{"g(n)":1,"lineas":1}),
        ("Maroussi","Neratziotissa",{"g(n)":1.6,"lineas":1}),
        ("Neratziotissa","Eirini",{"g(n)":3.4,"lineas":1}),
        ("Eirini","Iraklio",{"g(n)":1.6,"lineas":1}),
        ("Iraklio","Nea Ionia",{"g(n)":1.1,"lineas":1}),
        ("Nea Ionia","Pefkakia",{"g(n)":0.6,"lineas":1}),
        ("Pefkakia","Perissos",{"g(n)":0.7,"lineas":1}),
        ("Perissos","Ano Patisia",{"g(n)":1.3,"lineas":1}),
        ("Ano Patisia","Aghios Eleftherios",{"g(n)":0.6,"lineas":1}),
        ("Aghios Eleftherios","Kato Patisia",{"g(n)":1,"lineas":1}),
        ("Kato Patisia","Aghios Nikolaos",{"g(n)":0.5,"lineas":1}),
        ("Aghios Nikolaos","Attiki",{"g(n)":0.9,"lineas":1}),
        ("Attiki","Victoria",{"g(n)":1,"lineas":1}),
        ("Victoria","Omonia",{"g(n)":1,"lineas":1}),
        ("Omonia","Monastiraki",{"g(n)":0.6,"lineas":1}),
        ("Monastiraki","Thissio",{"g(n)":0.6,"lineas":1}),
        ("Thissio","Petralona",{"g(n)":0.9,"lineas":1}),
        ("Petralona","Tavros",{"g(n)":0.5,"lineas":1}),
        ("Tavros","Kalithea",{"g(n)":0.8,"lineas":1}),
        ("Kalithea","Moschato",{"g(n)":0.6,"lineas":1}),
        ("Moschato","Faliro",{"g(n)":0.8,"lineas":1}),
        ("Faliro","Piraeus",{"g(n)":1.1,"lineas":1}),

        ("Anthoupoli","Peristeri",{"g(n)":0.7,"lineas":2}),# Estacion Nueva!
        ("Peristeri","Aghios Antonios",{"g(n)":0.8,"lineas":2}),# Estacion Nueva!
        ("Aghios Antonios","Sepolia",{"g(n)":1.3,"lineas":2}),
        ("Sepolia","Attiki",{"g(n)":0.8,"lineas":2}),
        ("Attiki","Larissa Station",{"g(n)":0.8,"lineas":2}),
        ("Larissa Station","Metaxourghio",{"g(n)":0.7,"lineas":2}),
        ("Metaxourghio","Omonia",{"g(n)":0.6,"lineas":2}),
        ("Omonia","Panepistimio",{"g(n)":0.6,"lineas":2}),
        ("Panepistimio","Syntagma",{"g(n)":0.6,"lineas":2}),
        ("Syntagma","Akropoli",{"g(n)":0.9,"lineas":2}),
        ("Akropoli","Sygrou-Fix",{"g(n)":0.5,"lineas":2}),
        ("Sygrou-Fix","Neos Kosmos",{"g(n)":0.8,"lineas":2}),
        ("Neos Kosmos","Aghios Ioannis",{"g(n)":0.6,"lineas":2}),
        ("Aghios Ioannis","Dafni",{"g(n)":0.8,"lineas":2}),
        ("Dafni","Aghios Dimitrios",{"g(n)":1.1,"lineas":2}),
        ("Aghios Dimitrios","Ilioupoli",{"g(n)":1.3,"lineas":2}),# Estacion Nueva!
        ("Ilioupoli","Alimos",{"g(n)":1.3,"lineas":2}),# Estacion Nueva!
        ("Alimos","Argyroupoli",{"g(n)":1.7,"lineas":2}),# Estacion Nueva!
        ("Argyroupoli","Elliniko",{"g(n)":1.2,"lineas":2}),# Estacion Nueva!

        ("Nikaia","Korydallos",{"g(n)":2.1,"lineas":3}),
        ("Korydallos","Agia Varvara",{"g(n)":1.6,"lineas":3}),
        ("Agia Varvara","Egaleo",{"g(n)":1.4,"lineas":3}),
        ("Egaleo","Eleonas",{"g(n)":1.1,"lineas":3}),
        ("Eleonas","Kerameikos",{"g(n)":1.8,"lineas":3}),
        ("Kerameikos","Monastiraki",{"g(n)":1.2,"lineas":3}), 
        ("Monastiraki","Syntagma",{"g(n)":0.9,"lineas":3}),
        ("Syntagma","Evangelismos",{"g(n)":0.9,"lineas":3}),
        ("Evangelismos","Megaro Moussikis",{"g(n)":0.6,"lineas":3}),
        ("Megaro Moussikis","Ambelokipi",{"g(n)":1,"lineas":3}),
        ("Ambelokipi","Panormou",{"g(n)":0.9,"lineas":3}),
        ("Panormou","Katehaki",{"g(n)":1.1,"lineas":3}),
        ("Katehaki","Ethniki Amyna",{"g(n)":1,"lineas":3}),
        ("Ethniki Amyna","Holargos",{"g(n)":1.1,"lineas":3}),
        ("Holargos","Nomismatokopio",{"g(n)":1.1,"lineas":3}),
        ("Nomismatokopio","Aghia Paraskevi",{"g(n)":1.1,"lineas":3}),
        ("Aghia Paraskevi","Halandri",{"g(n)":0.9,"lineas":3}),
        ("Halandri","Doukissis Plakentias",{"g(n)":1.1,"lineas":3}),
        ("Doukissis Plakentias","Pallini",{"g(n)":3.9,"lineas":3}),
        ("Pallini","Paiania",{"g(n)":2.4,"lineas":3}),
        ("Paiania","Koropi",{"g(n)":8.2,"lineas":3}),# Estacion Nueva!
        ("Koropi","Airport",{"g(n)":5.1,"lineas":3})# Estacion Nueva!
        
    ]
    G.add_edges_from(Aristas)
    return G