#!/usr/bin/env python3
"""maze-runner-ai — generate mazes and watch DFS/BFS/A* solve them."""
import argparse, random, time, os, heapq, sys

def clear(): os.system("cls" if os.name=="nt" else "clear")

def gen_maze(size, seed=None):
    if size % 2 == 0: size += 1
    if seed: random.seed(seed)
    maze = [["#"] * size for _ in range(size)]
    def carve(x, y):
        dirs = [(0,2),(2,0),(0,-2),(-2,0)]; random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 < nx < size-1 and 0 < ny < size-1 and maze[nx][ny] == "#":
                maze[x+dx//2][y+dy//2] = " "; maze[nx][ny] = " "; carve(nx, ny)
    maze[1][1] = " "; carve(1, 1)
    maze[1][0] = "S"; maze[size-2][size-1] = "E"
    return maze, (1,0), (size-2, size-1)

def draw(maze, visited=None, path=None):
    ICONS = {"#":"█"," ":"·","S":"S","E":"E"}
    for r, row in enumerate(maze):
        line = ""
        for c, cell in enumerate(row):
            if path and (r,c) in path: line += "●"
            elif visited and (r,c) in visited: line += "░"
            else: line += ICONS.get(cell, cell)
        print(line)

def bfs(maze, start, end, animate):
    from collections import deque
    q = deque([(start, [start])]); visited = {start}
    while q:
        (r,c), path = q.popleft()
        if animate:
            clear(); draw(maze, visited, set(path)); time.sleep(0.03)
        if (r,c) == end: return path, visited
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r+dr,c+dc
            if 0<=nr<len(maze) and 0<=nc<len(maze[0]) and maze[nr][nc]!="#" and (nr,nc) not in visited:
                visited.add((nr,nc)); q.append(((nr,nc), path+[(nr,nc)]))
    return [], visited

def dfs(maze, start, end, animate):
    stack = [(start, [start])]; visited = set()
    while stack:
        (r,c), path = stack.pop()
        if (r,c) in visited: continue
        visited.add((r,c))
        if animate:
            clear(); draw(maze, visited, set(path)); time.sleep(0.02)
        if (r,c) == end: return path, visited
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r+dr,c+dc
            if 0<=nr<len(maze) and 0<=nc<len(maze[0]) and maze[nr][nc]!="#":
                stack.append(((nr,nc), path+[(nr,nc)]))
    return [], visited

def astar(maze, start, end, animate):
    def h(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])
    open_set = [(h(start,end), 0, start, [start])]; visited = set()
    while open_set:
        _, g, (r,c), path = heapq.heappop(open_set)
        if (r,c) in visited: continue
        visited.add((r,c))
        if animate:
            clear(); draw(maze, visited, set(path)); time.sleep(0.02)
        if (r,c) == end: return path, visited
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r+dr,c+dc
            if 0<=nr<len(maze) and 0<=nc<len(maze[0]) and maze[nr][nc]!="#" and (nr,nc) not in visited:
                ng = g+1; heapq.heappush(open_set,(ng+h((nr,nc),end),ng,(nr,nc),path+[(nr,nc)]))
    return [], visited

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--size",  type=int, default=21)
    p.add_argument("--algo",  default="astar", choices=["dfs","bfs","astar"])
    p.add_argument("--seed",  type=int, default=None)
    p.add_argument("--no-animate", action="store_true")
    a = p.parse_args()
    maze, start, end = gen_maze(a.size, a.seed)
    fn = {"dfs":dfs,"bfs":bfs,"astar":astar}[a.algo]
    path, visited = fn(maze, start, end, not a.no_animate)
    clear(); draw(maze, visited, set(path))
    print(f"\n{a.algo.upper()} | Path length: {len(path)} | Cells visited: {len(visited)}")

if __name__ == "__main__":
    main()
