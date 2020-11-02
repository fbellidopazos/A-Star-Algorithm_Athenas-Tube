from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import neighbors

G = nx.Graph()

Nodos = [
    ("Kifissia",{"h(n)":10,"lineas":[1] }),
    ("KAT",{"h(n)":10,"lineas":[1] }),
    ("Maroussi",{"h(n)":10,"lineas":[1] }),
    ("Neratziotissa",{"h(n)":10,"lineas":[1] }),
    ("Irini",{"h(n)":10,"lineas":[1] }),
    ("Iraklio",{"h(n)":10,"lineas":[1] }),
    ("Nea Ionia",{"h(n)":10,"lineas":[1] }),
    ("Pefkakia",{"h(n)":10,"lineas":[1] }),
    ("Perissos",{"h(n)":10,"lineas":[1] }),
    ("Ano Patisia",{"h(n)":10,"lineas":[1] }),
    ("Aghios Eleftherios",{"h(n)":10,"lineas":[1] }),
    ("Kato Patisia",{"h(n)":10,"lineas":[1] }),
    ("Aghios Nikolaos",{"h(n)":10,"lineas":[1] }),
    ("Attiki",{"h(n)":10,"lineas":[1,2] }),
    ("Victoria",{"h(n)":10,"lineas":[1] }),
    ("Omonia",{"h(n)":10,"lineas":[1,2] }),
    ("Monastiraki",{"h(n)":10,"lineas":[1,3] }),
    ("Thissio",{"h(n)":10,"lineas":[1] }),
    ("Petralona",{"h(n)":10,"lineas":[1] }),
    ("Tavros",{"h(n)":10,"lineas":[1] }),
    ("Kalithea",{"h(n)":10,"lineas":[1] }),
    ("Moschato",{"h(n)":10,"lineas":[1] }),
    ("Faliro",{"h(n)":10,"lineas":[1] }),
    ("Piraeus",{"h(n)":10,"lineas":[1] }),
    
    ("Aghios Antonios",{"h(n)":10,"lineas":[2] }),
    ("Sepolia",{"h(n)":10,"lineas":[2] }),
    ("Larissa Station",{"h(n)":10,"lineas":[2] }),
    ("Metaxourghio",{"h(n)":10,"lineas":[2] }),
    ("Panepistimio",{"h(n)":10,"lineas":[2] }),
    ("Syntagma",{"h(n)":10,"lineas":[2,3] }),
    ("Akropoli",{"h(n)":10,"lineas":[2] }),
    ("Sygrou-Fix",{"h(n)":10,"lineas":[2] }),
    ("Neos Kosmos",{"h(n)":10,"lineas":[2] }),
    ("Aghios Ioannis",{"h(n)":10,"lineas":[2] }),
    ("Dafni",{"h(n)":10,"lineas":[2] }),
    ("Aghios Dimitrios",{"h(n)":10,"lineas":[2] }),

    ("Egaleo",{"h(n)":10,"lineas":[3] }),
    ("Eleonas",{"h(n)":10,"lineas":[3] }),
    ("Kerameikos",{"h(n)":10,"lineas":[3] }),
    ("Evangelismos",{"h(n)":10,"lineas":[3] }),
    ("Megaro Moussikis",{"h(n)":10,"lineas":[3] }),
    ("Ambelokipi",{"h(n)":10,"lineas":[3] }),
    ("Panormou",{"h(n)":10,"lineas":[3] }),
    ("Katehaki",{"h(n)":10,"lineas":[3] }),
    ("Ethniki Amyna",{"h(n)":10,"lineas":[3] }),
    ("Holargos",{"h(n)":10,"lineas":[3] }),
    ("Nomismatokopio",{"h(n)":10,"lineas":[3] }),
    ("Aghia Paraskevi",{"h(n)":10,"lineas":[3] }),
    ("Halandri",{"h(n)":10,"lineas":[3] }),
    ("Doukissis Plakentias",{"h(n)":10,"lineas":[3] }),
    ("Pallini",{"h(n)":10,"lineas":[3] }),
    ("Paiania",{"h(n)":10,"lineas":[3] }),
    ("Koropi",{"h(n)":10,"lineas":[3] })
]

G.add_nodes_from(Nodos)

Aristas=[
    ("Kifissia","KAT",{"g(n)":20,"lineas":1}),
    ("KAT","Maroussi",{"g(n)":20,"lineas":1}),
    ("Maroussi","Neratziotissa",{"g(n)":20,"lineas":1}),
    ("Neratziotissa","Irini",{"g(n)":20,"lineas":1}),
    ("Irini","Iraklio",{"g(n)":20,"lineas":1}),
    ("Iraklio","Nea Ionia",{"g(n)":20,"lineas":1}),
    ("Nea Ionia","Pefkakia",{"g(n)":20,"lineas":1}),
    ("Pefkakia","Perissos",{"g(n)":20,"lineas":1}),
    ("Perissos","Ano Patisia",{"g(n)":20,"lineas":1}),
    ("Ano Patisia","Aghios Eleftherios",{"g(n)":20,"lineas":1}),
    ("Aghios Eleftherios","Kato Patisia",{"g(n)":20,"lineas":1}),
    ("Kato Patisia","Aghios Nikolaos",{"g(n)":20,"lineas":1}),
    ("Aghios Nikolaos","Attiki",{"g(n)":20,"lineas":1}),
    ("Attiki","Victoria",{"g(n)":20,"lineas":1}),
    ("Victoria","Omonia",{"g(n)":20,"lineas":1}),
    ("Omonia","Monastiraki",{"g(n)":20,"lineas":1}),
    ("Monastiraki","Thissio",{"g(n)":20,"lineas":1}),
    ("Thissio","Petralona",{"g(n)":20,"lineas":1}),
    ("Petralona","Tavros",{"g(n)":20,"lineas":1}),
    ("Tavros","Kalithea",{"g(n)":20,"lineas":1}),
    ("Kalithea","Moschato",{"g(n)":20,"lineas":1}),
    ("Moschato","Faliro",{"g(n)":20,"lineas":1}),
    ("Faliro","Piraeus",{"g(n)":20,"lineas":1}),

    ("Aghios Antonios","Sepolia",{"g(n)":20,"lineas":2}),
    ("Sepolia","Attiki",{"g(n)":20,"lineas":2}),
    ("Attiki","Larissa Station",{"g(n)":20,"lineas":2}),
    ("Larissa Station","Metaxourghio",{"g(n)":20,"lineas":2}),
    ("Metaxourghio","Omonia",{"g(n)":20,"lineas":2}),
    ("Omonia","Panepistimio",{"g(n)":20,"lineas":2}),
    ("Panepistimio","Syntagma",{"g(n)":20,"lineas":2}),
    ("Syntagma","Akropoli",{"g(n)":20,"lineas":2}),
    ("Akropoli","Sygrou-Fix",{"g(n)":20,"lineas":2}),
    ("Sygrou-Fix","Neos Kosmos",{"g(n)":20,"lineas":2}),
    ("Neos Kosmos","Aghios Ioannis",{"g(n)":20,"lineas":2}),
    ("Aghios Ioannis","Dafni",{"g(n)":20,"lineas":2}),
    ("Dafni","Aghios Dimitrios",{"g(n)":20,"lineas":2}),

    ("Egaleo","Eleonas",{"g(n)":20,"lineas":3}),
    ("Eleonas","Kerameikos",{"g(n)":20,"lineas":3}),
    ("Kerameikos","Monastiraki",{"g(n)":20,"lineas":3}), 
    ("Monastiraki","Syntagma",{"g(n)":20,"lineas":3}),
    ("Syntagma","Evangelismos",{"g(n)":20,"lineas":3}),
    ("Evangelismos","Megaro Moussikis",{"g(n)":20,"lineas":3}),
    ("Megaro Moussikis","Ambelokipi",{"g(n)":20,"lineas":3}),
    ("Ambelokipi","Panormou",{"g(n)":20,"lineas":3}),
    ("Panormou","Katehaki",{"g(n)":20,"lineas":3}),
    ("Katehaki","Ethniki Amyna",{"g(n)":20,"lineas":3}),
    ("Ethniki Amyna","Holargos",{"g(n)":20,"lineas":3}),
    ("Holargos","Nomismatokopio",{"g(n)":20,"lineas":3}),
    ("Nomismatokopio","Aghia Paraskevi",{"g(n)":20,"lineas":3}),
    ("Aghia Paraskevi","Halandri",{"g(n)":20,"lineas":3}),
    ("Halandri","Doukissis Plakentias",{"g(n)":20,"lineas":3}),
    ("Doukissis Plakentias","Pallini",{"g(n)":20,"lineas":3}),
    ("Pallini","Paiania",{"g(n)":20,"lineas":3}),
    ("Paiania","Koropi",{"g(n)":20,"lineas":3})
    
]

G.add_edges_from(Aristas)



color_map=['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'green', 'green', 'red', 'red', 'green', 'blue', 'blue', 'green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']


neighbors=["Test"]
neighbors.extend([i for i in G.neighbors("Attiki")])

print(neighbors)


print(G.edges[("Attiki","Victoria")]["g(n)"])
nx.draw_kamada_kawai(G,with_labels=True,edge_color=color_map,node_size=300,width=7,font_size=9)
#nx.draw_networkx(G,with_labels=True,edge_color=color_map[::-1],node_size=300,width=5)
plt.legend(["Estaciones"])
plt.show()