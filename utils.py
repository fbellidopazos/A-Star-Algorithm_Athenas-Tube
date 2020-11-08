import networkx as nx

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

def heuristic():
    return 0

def getAtenas():
    G = nx.Graph()

    Nodos = [
        ("Kifissia",{"lineas":[1],"coordenadas":(38.0736817,23.8083101) }),
        ("KAT",{"lineas":[1], "coordenadas":(38.065833, 23.803889)}),
        ("Maroussi",{"lineas":[1] }),
        ("Neratziotissa",{"lineas":[1] }),
        ("Irini",{"lineas":[1] }),
        ("Iraklio",{"lineas":[1] }),
        ("Nea Ionia",{"lineas":[1] }),
        ("Pefkakia",{"lineas":[1] }),
        ("Perissos",{"lineas":[1] }),
        ("Ano Patisia",{"lineas":[1] }),
        ("Aghios Eleftherios",{"lineas":[1] }),
        ("Kato Patisia",{"lineas":[1] }),
        ("Aghios Nikolaos",{"lineas":[1] }),
        ("Attiki",{"lineas":[1,2] }),
        ("Victoria",{"lineas":[1] }),
        ("Omonia",{"lineas":[1,2] }),
        ("Monastiraki",{"lineas":[1,3] }),
        ("Thissio",{"lineas":[1] }),
        ("Petralona",{"lineas":[1] }),
        ("Tavros",{"lineas":[1] }),
        ("Kalithea",{"lineas":[1] }),
        ("Moschato",{"lineas":[1] }),
        ("Faliro",{"lineas":[1] }),
        ("Piraeus",{"lineas":[1] }),
        
        ("Anthoupoli",{"lineas":[2] }),# Estacion Nueva!
        ("Peristeri",{"lineas":[2] }),# Estacion Nueva!
        ("Aghios Antonios",{"lineas":[2] }),
        ("Sepolia",{"lineas":[2] }),
        ("Larissa Station",{"lineas":[2] }),
        ("Metaxourghio",{"lineas":[2] }),
        ("Panepistimio",{"lineas":[2] }),
        ("Syntagma",{"lineas":[2,3] }),
        ("Akropoli",{"lineas":[2] }),
        ("Sygrou-Fix",{"lineas":[2] }),
        ("Neos Kosmos",{"lineas":[2] }),
        ("Aghios Ioannis",{"lineas":[2] }),
        ("Dafni",{"lineas":[2] }),
        ("Aghios Dimitrios",{"lineas":[2] }),
        ("Ilioupoli",{"lineas":[2] }),# Estacion Nueva!
        ("Alimos",{"lineas":[2] }),# Estacion Nueva!
        ("Argyroupoli",{"lineas":[2] }),# Estacion Nueva!
        ("Elliniko",{"lineas":[2] }),# Estacion Nueva!

        ("Aghia Marina",{"lineas":[3] }),# Estacion Nueva!
        ("Egaleo",{"lineas":[3] }),
        ("Eleonas",{"lineas":[3] }),
        ("Kerameikos",{"lineas":[3] }),
        ("Evangelismos",{"lineas":[3] }),
        ("Megaro Moussikis",{"lineas":[3] }),
        ("Ambelokipi",{"lineas":[3] }),
        ("Panormou",{"lineas":[3] }),
        ("Katehaki",{"lineas":[3] }),
        ("Ethniki Amyna",{"lineas":[3] }),
        ("Holargos",{"lineas":[3] }),
        ("Nomismatokopio",{"lineas":[3] }),
        ("Aghia Paraskevi",{"lineas":[3] }),
        ("Halandri",{"lineas":[3] }),
        ("Doukissis Plakentias",{"lineas":[3] }),
        ("Pallini",{"lineas":[3] }),
        ("Paiania",{"lineas":[3] }),
        ("Koropi",{"lineas":[3] }),
        ("Airport",{"lineas":[3] })
    ]
    G.add_nodes_from(Nodos)

    Aristas=[
        ("Kifissia","KAT",{"g(n)":1,"lineas":1}),
        ("KAT","Maroussi",{"g(n)":1,"lineas":1}),
        ("Maroussi","Neratziotissa",{"g(n)":1.6,"lineas":1}),
        ("Neratziotissa","Irini",{"g(n)":3.4,"lineas":1}),
        ("Irini","Iraklio",{"g(n)":1.6,"lineas":1}),
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

        ("Aghia Marina","Egaleo",{"g(n)":1.4,"lineas":3}),
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