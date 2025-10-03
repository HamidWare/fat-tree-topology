import networkx as nx

# Parameters
k = 8
G = nx.Graph()

count = 0

# Servers
servers = []
for pod in range(k):
    for sw in range(k // 2):
        for srv in range(k // 2):
            server = str(count)
            servers.append(server)
            G.add_node(server, type='Server')
            count += 1

# Edge Switches
edge_switches = []
for pod in range(k):
    for sw in range(k // 2):
        edge = str(count)
        edge_switches.append(edge)
        G.add_node(edge, type='Edge')
        count += 1

# Aggregation Switches
agg_switches = []
for pod in range(k):
    for sw in range(k // 2):
        agg = str(count)
        agg_switches.append(agg)
        G.add_node(agg, type='Agg')
        count += 1

# Core Switches
core_switches = []
for i in range((k // 2) ** 2):
    core = str(count)
    core_switches.append(core)
    G.add_node(core, type='Core')
    count += 1

# Connect Servers to Edge Switches
for i, edge in enumerate(edge_switches):
    for server in servers[i * (k // 2):(i + 1) * (k // 2)]:
        G.add_edge(edge, server)

# Connect Edge to Aggregation
for pod in range(0, len(edge_switches), k // 2):
    for i, edge in enumerate(edge_switches[pod:pod + (k // 2)]):
        for j, agg in enumerate(agg_switches[pod:pod + (k // 2)]):
            G.add_edge(edge, agg)
            # make sure node 24 connects to nodes 32 and 33
            if j == 0:
                G.add_edge(agg, core_switches[i])
            elif j == 1:
                G.add_edge(agg, core_switches[i + (k // 2)])

# find shortest paths
def find_and_export_all_shortest_paths(node1, node2):
    if not G.has_node(node1) or not G.has_node(node2):
        print("Node1 and/or Node2 not found in the graph.")
        return

    try:
        all_shortest_paths = list(nx.all_shortest_paths(G, source=node1, target=node2))

        if not all_shortest_paths:
            print(f"No paths found between {node1} and {node2}.")
        else:
            # Export shortest paths
            csv_filename = 'all_shortest_paths.csv'
            with open(csv_filename, 'w') as csvfile:
                csvfile.write('Shortest Paths\n')
                for path in all_shortest_paths:
                    path_string = ' ---> '.join(map(str, path))
                    csvfile.write(f'{path_string}\n')
            
            print(f"All shortest paths are saved to {csv_filename}.")
            print("All Shortest Paths:")
            for i, path in enumerate(all_shortest_paths):
                path_string = ' ---> '.join(map(str, path))
                print(f"Path {i + 1}: {path_string}")
    except nx.NetworkXNoPath:
        print(f"No paths found between {node1} and {node2}.")

# Input nodes
node1 = input("Enter Node 1: ")
node2 = input("Enter Node 2: ")

find_and_export_all_shortest_paths(node1, node2)
