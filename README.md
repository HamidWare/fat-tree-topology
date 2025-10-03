# Fat-Tree Topology (k=4 / k=8) — Python + NetworkX

This repo implements a classic fat-tree datacenter topology and explores shortest paths between hosts using NetworkX. It contains two small scripts aligned with a two-phase class assignment.

<p align="center">
  <img src="images/part_1_Figure.png" alt="Fat-tree layout (k=4)" width="520">
</p>

## Features
- Phase 1 (k=4): builds the fat-tree graph, exports the link table to `data/fat_tree.csv`, and draws a layered visualization.
- Phase 2 (k=8): builds the fat-tree graph and exports **all shortest simple paths** between two input nodes to `data/all_shortest_paths.csv`.

## Project structure
- src/ # Python scripts
- data/ # CSV outputs
- images/ # Visualization(s)
- docs/ # Assignment brief

## Usage
**Phase 1: Build and visualize (k=4)**

python src/phase1_fattree.py

Outputs:
* data/fat_tree.csv (edge list with “Arc exist” column)
* An on-screen plot of the fat-tree (saved manually if desired)

**Phase 2: All shortest paths (k=8)**

python src/phase2_all_shortest_paths.py

Enter two node IDs (as strings) when prompted, e.g.:
- Enter Node 1: 0
- Enter Node 2: 8

Outputs
* data/all_shortest_paths.csv where each row lists one shortest path
* All paths also printed to stdout

## Data
* data/fat_tree.csv – Phase 1 link table
* data/all_shortest_paths.csv – Phase 2 path enumeration
* docs/Assignment1.pdf – Original Persian project description

## Citation
If you use this in a report, please cite the repository link and include the assignment as supplementary material.

## License
MIT (see LICENSE).
