import numpy as np

def dfs(src, target):
  stack = []     # nodes to be explored
  stack.append(src)
  exp = []       # nodes already explored


  while len(stack) > 0:
    source = stack.pop()
    exp.append(source)

    print_puzzle(src)

    if source == target:
      print()
      print("Success! Goal state reached!")
      return

    # if direction possible then add that state
    poss_moves_to_do = possible_moves(source, exp)

    for move in poss_moves_to_do:
      if move not in stack and move not in exp:
        stack.append(move)

def possible_moves(state, visited_states):
  b = state.index(0)            # index of empty tile
  d = []                        # directions array

  if b not in [0, 1, 2]:
    d.append('u')
  if b not in [6, 7, 8]:
    d.append('d')
  if b not in [0, 3, 6]:
    d.append('l')
  if b not in [2, 5, 8]:
    d.append('r')

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

src = [1, 2, 3, 4, 5, 6, 0, 7, 8]
target = [1, 2, 3, 4, 5, 6, 7, 8, 0]

print("Initial state:")
print_puzzle(src)
print()

print("Goal state")
print_puzzle(target)
print()

print("DFS solution:")
dfs(src, target)
