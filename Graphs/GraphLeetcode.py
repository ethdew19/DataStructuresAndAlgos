#Leetcode #200. Number of Islands
#https://leetcode.com/problems/number-of-islands/

#General strategy: Loop through every point in the graph. Run a DFS at that point. Track every node it reaches in a set. That way, any time you reach a node and it hasn't been visited you know its and island
def numIslands(grid):
    count = 0
    visited = set()
    for index,list in enumerate(grid):
        for indexj, j in enumerate(list):
            if (index,indexj) not in visited:
                if grid[index][indexj] == "1":
                    count += 1
                    visited = dfs(grid,visited,(index,indexj))
    return count
def dfs(grid,visited,coords):
    if coords not in visited and grid[coords[0]][coords[1]] == "1":
        visited.add(coords)
        if coords[0] > 0:
            dfs(grid,visited,(coords[0] - 1,coords[1]))
        if coords[0] < len(grid) - 1:
            dfs(grid,visited,(coords[0] + 1, coords[1]))
        if coords[1] > 0:
            dfs(grid,visited,(coords[0],coords[1] - 1))
        if coords[1] < len(grid[0]) - 1:
            dfs(grid,visited,(coords[0],coords[1] + 1))
    return visited

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


print(numIslands(grid)) #Prints 1
print(numIslands(grid2)) #Prints 2

