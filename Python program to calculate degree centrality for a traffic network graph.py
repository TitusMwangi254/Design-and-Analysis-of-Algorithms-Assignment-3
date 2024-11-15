import networkx as nx

def calculate_degree_centrality(graph):
    """
    Calculate degree centrality for a graph.
    
    :param graph: A NetworkX graph.
    :return: Dictionary of nodes with their degree centrality values.
    """
    return nx.degree_centrality(graph)

def main():
    # Create a traffic network graph
    traffic_network = nx.Graph()
    
    # Add edges representing roads between intersections
    traffic_network.add_edges_from([
        ("A", "B"), ("A", "C"), ("B", "C"), 
        ("B", "D"), ("C", "E"), ("D", "E"), 
        ("E", "F"), ("D", "F")
    ])
    
    # Calculate degree centrality
    degree_centralities = calculate_degree_centrality(traffic_network)
    
    print("Degree Centrality of intersections:")
    for intersection, centrality in degree_centralities.items():
        print(f"Intersection {intersection}: {centrality:.3f}")

if __name__ == "__main__":
    main()
