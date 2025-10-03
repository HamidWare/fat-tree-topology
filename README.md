# Fat-Tree Topology (k=4 / k=8) — Python + NetworkX

This repo implements a classic fat-tree datacenter topology and explores shortest paths between hosts using NetworkX. It contains two small scripts aligned with a two-phase class assignment.

<p align="center">
  <img src="images/part_1_Figure.png" alt="Fat-tree layout (k=4)" width="520">
</p>

## Features
- Phase 1 (k=4): builds the fat-tree graph, exports the link table to `data/fat_tree.csv`, and draws a layered visualization.
- Phase 2 (k=8): builds the fat-tree graph and exports **all shortest simple paths** between two input nodes to `data/all_shortest_paths.csv`.

## Project structure
