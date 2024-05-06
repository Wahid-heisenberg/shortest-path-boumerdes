import networkx as nx
import matplotlib.pyplot as plt
import json
import math
from town_functions import find_bordering_towns

# Load town coordinates from JSON file
with open("town_coordinates.json", "r") as json_file:
    data = json.load(json_file)

# Create a graph
G = nx.Graph()

# Add nodes with town names and coordinates
for town_data in data:
    town = town_data["town"]
    coordinates = tuple(town_data["coordinates"])
    G.add_node(town, pos=coordinates)

# Get bordering towns for each town
bordering_towns = find_bordering_towns(data)

# Calculate Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Calculate edge weights (Euclidean distances) and add edges between bordering towns
for town, neighbors in bordering_towns.items():
    for neighbor in neighbors:
        if G.has_node(neighbor):
            u_coords = G.nodes[town]["pos"]
            v_coords = G.nodes[neighbor]["pos"]
            distance = euclidean_distance(u_coords, v_coords)
            G.add_edge(town, neighbor, weight=distance)

# Draw the graph
plt.figure(figsize=(12, 10))

# Adjust node size and font size
node_size = 3000
font_size = 10

# Adjust spacing between nodes
pos = nx.spring_layout(G, k=0.4)  # Adjust k for spacing

# Draw nodes with custom node colors and edge styles
nx.draw(G, pos, node_size=node_size, node_color='lightblue', edge_color='grey', width=1.0)

# Draw node labels with content centered
labels = nx.get_node_attributes(G, 'pos')
for node, (x, y) in pos.items():
    formatted_coords = f"{x:.2f}, {y:.2f}"
    plt.text(x, y, f"{node}\n{formatted_coords}", horizontalalignment='center', verticalalignment='center', fontsize=font_size)

plt.title("Graph of Towns with Shared Borders")
plt.show()

# Find shortest path between two nodes using Dijkstra's algorithm
source_node = "Ammal"  # Example source node
target_node = "Corso"  # Example target node
shortest_path = nx.shortest_path(G, source=source_node, target=target_node, weight="weight")
print(f"Shortest path from {source_node} to {target_node}: {shortest_path}")
