import numpy as np

def bfs(src, target):
  queue = []         # nodes to be explored
  queue.append(src)
  exp = []           # nodes already explored

  while len(queue) > 0:
    source = queue.pop(0)
    exp.append(source)

    print_puzzle(source)

    if source == target:
      print()
      print("Success! Goal state achieved!")
      return

    # if direction possbile then add state to move
    poss_moves_to_do = possible_moves(source, exp)

    for move in poss_moves_to_do:
      if move not in exp and move not in queue:
        queue.append(move)

def possible_moves(state, visited_states):
  b = state.index(0)      # loc of empty tile
  d = []                  # directions array

  if b not in [0, 1, 2]:
    d.append('u')
  if b not in [6, 7, 8]:
    d.append('d')
  if b not in [0, 3, 6]:
    d.append('l')
  if b not in [2, 5, 8]:
    d.append('r')

  # for all possible moves, the state that will be reached on playing that
  pos_moves_it_can = []
  for i in d:
    pos_moves_it_can.append(gen(state, i, b))
  return [move_it_can for move_it_can in pos_moves_it_can if move_it_can not in visited_states]

def gen(state, m, b):
  temp = state.copy()

  if m == 'd':
    temp[b+3], temp[b] = temp[b], temp[b+3]
  if m == 'u':
    temp[b-3], temp[b] = temp[b], temp[b-3]
  if m == 'l':
    temp[b-1], temp[b] = temp[b], temp[b-1]
  if m == 'r':
    temp[b+1], temp[b] = temp[b], temp[b+1]
  return temp

def print_puzzle(state):
  print(np.array(state).reshape(3, 3))
  print()

initial = [1, 2, 3, 4, 5, 6, 0, 7, 8]
target = [1, 2, 3, 4, 5, 6, 7, 8, 0]

print("Initial state:")
print_puzzle(initial)
print()

print("Goal state:")
print_puzzle(target)
print()

print("BFS solution:")
bfs(initial, target)
