import random
import time

import matplotlib.pyplot as plt
import networkx as nx


class LSRA_Baseline:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def shortest_path(self, source, target):
        # Initialize distances to infinity
        distances = {node: float('inf') for node in self.graph.nodes()}
        distances[source] = 0

        # Relax edges repeatedly
        for _ in range(len(self.graph.nodes()) - 1):
            for node1, node2 in self.graph.edges():
                distances[node2] = min(distances[node2], distances[node1] + self.graph[node1][node2]['weight'])

        return distances  # Return distances instead of a single value

if __name__ == "__main__":
    lsra_baseline = LSRA_Baseline()

    # Add 50 nodes with random edges and weights
    for i in range(50):
        lsra_baseline.graph.add_node(str(i))
    for i in range(50):
        for j in range(i+1, 50):
            if random.random() < 0.2:  # Probability of having an edge between nodes
                lsra_baseline.add_edge(str(i), str(j), random.randint(1, 100))

    # Visualization
    pos = nx.spring_layout(lsra_baseline.graph)  
    nx.draw(lsra_baseline.graph, pos, with_labels=True, node_size=700)  
    edge_labels = nx.get_edge_attributes(lsra_baseline.graph, 'weight')  
    nx.draw_networkx_edge_labels(lsra_baseline.graph, pos, edge_labels=edge_labels)  
    plt.title('Network Graph')
    plt.show()

    # Calculate shortest paths from source node '0'
    source_node = '0'
    start_time = time.time()
    shortest_paths = lsra_baseline.shortest_path(source_node, '49')
    end_time = time.time()
    total_time = end_time - start_time

    # Print shortest paths and total time taken
    print(f"Shortest paths from node {source_node}:")
    for target, distance in shortest_paths.items():
        print(f"To node {target}: Distance: {distance}")
    print("Total time taken:", total_time, "seconds")

    # Calculate the number of nodes and edges in the graph
    num_nodes = len(lsra_baseline.graph.nodes())
    num_edges = len(lsra_baseline.graph.edges())

    # Print the estimated time complexity category
    time_complexity_category = "O(n^2) Time Complexity"
    print(f"Estimated time complexity category for LSRA: {time_complexity_category}")