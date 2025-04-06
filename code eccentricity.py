Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import networkx as nx
... import matplotlib.pyplot as plt
... import numpy as np
... from collections import defaultdict
... 
... # Function to compute eccentricity
... def compute_eccentricity(G):
...     return nx.eccentricity(G)
... 
... # Function to draw the graph and classify edges by their endpoint eccentricities
... def draw_and_classify_edges_by_eccentricity(adj_matrix):
...     # Create a graph from the adjacency matrix
...     G = nx.from_numpy_array(np.array(adj_matrix)) # Use from_numpy_array instead of from_numpy_matrix
... 
...     # Draw the graph
...     pos = nx.spring_layout(G)  # positions for all nodes
...     nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='k', linewidths=1, font_size=15)
... 
...     # Compute eccentricities for each node
...     eccentricities = compute_eccentricity(G)
... 
...     # Print the eccentricity of each vertex
...     print("Eccentricity of each vertex:")
...     for node, ecc in eccentricities.items():
...         print(f"Node {node}: {ecc}")
... 
...     # Classify edges by their endpoint eccentricities
...     edge_class = {}
...     eccentricity_count = defaultdict(int)
... 
...     for edge in G.edges():
...         # Get eccentricities of each vertex in the edge
...         ecc = tuple(sorted((eccentricities[edge[0]], eccentricities[edge[1]])))
...         edge_class[edge] = ecc
...         # Increment the count of this type of edge
        eccentricity_count[ecc] += 1

    # Highlight edges by their classification
    edge_colors = ['blue' if ecc == (2, 3) else 'red' for edge, ecc in edge_class.items()]
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors)

    # Show the graph
    plt.show()

    return edge_class, eccentricity_count

# Example adjacency matrix
adjacency_matrix = [
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],    #Row#1
[1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],    #Row#2
[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],    #Row#3
[0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],    #Row#4
[0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],    #Row#5
[0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],    #Row#6
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],    #Row#7
[0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],    #Row#8
[0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],    #Row#9
[0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0],    #Row#10
[0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],    #Row#11
[0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0],    #Row#12
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],    #Row#13
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],    #Row#14
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],    #Row#15
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],    #Row#16
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],    #Row#17
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],    #Row#18
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]    #Row#19
]

# Call the function with the adjacency matrix
edge_classification, frequency_of_edges = draw_and_classify_edges_by_eccentricity(adjacency_matrix)
print("Edge Classification by eccentricity:", edge_classification)
print("Frequency of each type of edge:", frequency_of_edges)

