import networkx as nx
import matplotlib.pyplot as plt
import json
from town_functions import find_bordering_towns, haversine  # Import the haversine function

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

# Calculate edge weights (Haversine distances) and add edges between bordering towns
for town, neighbors in bordering_towns.items():
    for neighbor in neighbors:
        if G.has_node(neighbor):
            u_coords = G.nodes[town]["pos"]
            v_coords = G.nodes[neighbor]["pos"]
            # Use haversine distance instead of euclidean distance
            distance = haversine(u_coords, v_coords)
            G.add_edge(town, neighbor, weight=distance)

# Find shortest path between two nodes using A* algorithm and haversine distance
source_node = "Ammal"  # Example source node
target_node = "Corso"  # Example target node

shortest_path = nx.shortest_path(G, source=source_node, target=target_node, weight="weight", method="dijkstra")

# Draw the graph using Fruchterman-Reingold layout
plt.figure(figsize=(12, 10))
node_size = 3000
font_size = 10
pos = nx.fruchterman_reingold_layout(G)

# Draw nodes with custom node colors and edge styles
nx.draw(G, pos, node_size=node_size, node_color='lightblue', edge_color='grey', width=1.0)

# Draw node labels with content centered
labels = nx.get_node_attributes(G, 'pos')
for node, (x, y) in pos.items():
    formatted_coords = f"{x:.2f}, {y:.2f}"
    plt.text(x, y, f"{node}\n{formatted_coords}", horizontalalignment='center', verticalalignment='center', fontsize=font_size)

# Highlight the shortest path edges with blue color
path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]

nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', width=2.0)

plt.title("Graph of Towns with Shared Borders")
plt.show()

print(f"Shortest path from {source_node} to {target_node}: {shortest_path}")
