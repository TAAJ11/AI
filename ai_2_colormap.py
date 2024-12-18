# func to check if current color assignment is safe for vertex
def is_safe(vertex, graph, colors, color, assigned_colors):
  for i in range(len(graph)):
    if graph[vertex][i] == 1 and assigned_colors[i] == color:
      return False
  return True

# func to print current state of color assignment
def print_assignment(assigned_colors, step):
  print(f"Step: {step}: {assigned_colors}")

# func to solve map-coloring problem using backtracking
def map_coloring(graph, colors, assigned_colors, vertex, step):
  if vertex == len(graph):
    return True                   # if all vertices have been assigned color then returns true

  # try different colors for current state
  for color in colors:
     if is_safe(vertex, graph, colors, color, assigned_colors):
      assigned_colors[vertex] = color              # assign color to vertex
      print_assignment(assigned_colors, step)
      step += 1

      if map_coloring(graph, colors, assigned_colors, vertex + 1, step):        # recursion to assign colors to other vertices
        return True

      assigned_colors[vertex] = None            # if assigning colors didn't work then backtracking
      print(f"Backtrack from step: {step}")
  return False

def solve_map_coloring(graph, colors):
  assigned_colors = [None] * len(graph)           # initialize all vertices as unassigned
  step = 1

  if not map_coloring(graph, colors, assigned_colors, 0, step):
    print("No solution exists!")
    return None

  return assigned_colors

# Adjacency matrix of the map (Graph)
graph = [
    [0, 1, 0, 1],  # Region 1 is connected to Region 2 and Region 4
    [1, 0, 1, 1],  # Region 2 is connected to Region 1, Region 3, and Region 4
    [0, 1, 0, 1],  # Region 3 is connected to Region 2 and Region 4
    [1, 1, 1, 0]   # Region 4 is connected to Region 1, Region 2, and Region 3
]

# graph = [
#     [0, 1, 0, 1, 0],  # Region 1 is connected to Region 2 and Region 4
#     [1, 0, 1, 1, 1],  # Region 2 is connected to Region 1, Region 3, Region 4, and Region 5
#     [0, 1, 0, 0, 1],  # Region 3 is connected to Region 2 and Region 5
#     [1, 1, 0, 0, 1],  # Region 4 is connected to Region 1, Region 2, and Region 5
#     [0, 1, 1, 1, 0]   # Region 5 is connected to Region 2, Region 3, and Region 4
# ]

colors = ["Red", "Green", "Blue"]                 # list of available colors

solution = solve_map_coloring(graph, colors)

if solution:
  print()
  print(f"Final solution: {solution}")
