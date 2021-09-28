import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
for i in range(1, 11):
    G.add_node(i)
    G.add_edge(i, i + 1)
    if i == 11 - 1:
        G.add_edge(1, 11)

print(G.number_of_nodes())
print(G.number_of_edges())

plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.savefig('plot.png', dpi=300, bbox_inches='tight')