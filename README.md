<div align="center">

# 🧩 maze-runner-ai

**Generate random mazes and watch AI solve them in real time.**  
DFS, BFS, and A* — all visualised live in the terminal.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

---

## What is this?

I built this to actually *see* the difference between pathfinding algorithms — not just read about them. Watch DFS dive deep into dead ends, BFS fan out layer by layer, and A* zoom straight to the exit.

Every step is animated in the terminal so you can watch the logic happen in real time.

---

## Algorithms

| Algorithm | Strategy | Optimal path? | Speed |
|---|---|---|---|
| DFS | Goes deep first, backtracks | ❌ | Fast |
| BFS | Explores layer by layer | ✅ (unweighted) | Medium |
| A* | Uses heuristic (Manhattan distance) | ✅ | Fastest |

---

## Usage

```bash
python maze.py                        # random 21x21 maze, A* solver
python maze.py --algo bfs             # use BFS
python maze.py --algo dfs             # use DFS
python maze.py --size 41              # bigger maze (must be odd)
python maze.py --seed 7 --algo astar  # reproducible
python maze.py --no-animate           # instant result, no animation
```

---

## Built by

[@AadhhyaSharma](https://github.com/AadhhyaSharma) — 15-year-old builder from Jaipur 🇮🇳  
Built to visualise and actually understand pathfinding algorithms.
