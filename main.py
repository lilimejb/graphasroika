import networkx as nx
import matplotlib.pyplot as plt
import os


class GraphMaker:
    def __init__(self, matrix):
        self.matrix = [[bool(num) for num in elem] for elem in matrix]
        self.graph = nx.Graph()

    def builder(self):
        [self.graph.add_node(i) for i in range(1, len(self.matrix) + 1)]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    self.graph.add_edge(i + 1, j + 1)
                    

    def make_image(self):
        self.builder()
        plt.subplot(121)
        nx.draw(self.graph, with_labels=True, font_weight='bold')
        plt.savefig('plot.png', dpi=300, bbox_inches='tight')
        plt.clf()
