# Labyrinth-Maze-


# Labyrinth Analysis Project

## Overview
This project is a Python-based solution to analyze labyrinth structures represented by a specific coding system. The labyrinth is represented in text files using the numbers {0, 1, 2, 3}, where each digit signifies different types of connections between points in the grid.

## Features
The program processes the labyrinth structure from a text file and outputs detailed information about the labyrinth, including:
- **Number of Gates:** Openings in the labyrinth walls.
- **Connected Wall Sets:** Groups of walls that are interconnected.
- **Inaccessible Inner Points:** Points that cannot be reached from any gate.
- **Accessible Areas:** Regions of the labyrinth that can be accessed from at least one gate.
- **Accessible Cul-de-sacs:** Dead-end paths that can be accessed from a gate.
- **Entry-Exit Paths:** Paths that go from one gate to another without intersections or leading into a cul-de-sac.

## Algorithms Used
### Depth-First Search (DFS)
DFS is a fundamental algorithm used in this project to explore the labyrinth. The algorithm starts from a gate and traverses through all connected paths to identify:
- **Connected Wall Sets:** By traversing the labyrinth, DFS helps identify which walls are interconnected.
- **Accessible Areas:** DFS helps in determining the regions of the labyrinth that are reachable from the gates.

### Dead End Filling
The Dead End Filling algorithm is utilized to identify cul-de-sacs in the labyrinth. This technique involves iteratively filling in paths that lead to dead ends, effectively isolating those sections of the labyrinth:
- **Accessible Cul-de-sacs:** By filling in dead ends, the algorithm identifies paths that have no further extensions and classifies them as cul-de-sacs.

## How to Run the Program
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/labyrinth-analysis.git
   cd labyrinth-analysis
   ```

2. Ensure you have Python installed (version 3.6 or above is recommended).

3. Place your labyrinth text file in the same directory as the Python script (`labyrinth.py`).

4. Run the script with the filename as an argument:
   ```bash
   python labyrinth.py labyrinth_1.txt
   ```

5. The output will display the various features of the labyrinth as described in the Features section.

## Example
Given a sample labyrinth file `labyrinth_1.txt`:
```
1 0 2 2 1 2 3 0
3 2 2 1 2 0 2 2
3 0 1 1 3 1 0 0
2 0 3 0 0 1 2 0
3 2 2 0 1 2 3 2
1 0 0 1 1 0 0 0
```

The program would output:
```
The labyrinth has 2 gates.
The labyrinth has 3 sets of walls that are all connected.
The labyrinth has 4 inaccessible inner points.
The labyrinth has 1 accessible area.
The labyrinth has 2 sets of accessible cul-de-sacs that are all connected.
The labyrinth has 1 entry-exit path with no intersections not to cul-de-sacs.
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
