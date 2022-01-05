import numpy as np
from pandas import DataFrame, set_option
import networkx as nx
import pylab as plt
import visualization

ROWS  =  10
COLS  =  10
GAMMA = 0.8

Q = np.zeros((ROWS, COLS))
R = np.array([
                      
  [  0,    0,   -1,   -1,   -1,   -1,   -1,   -1,    0,   -1 ],
  [  0,   -1,    0,   -1,   -1,   -1,   -1,   -1,   -1,   -1 ],
  [ -1,    0,   -1,    0,   -1,   -1,   -1,   -1,   -1,   -1 ],
  [ -1,   -1,    0,   -1,   -1,   -1,    0,   -1,   -1,   -1 ],
  [ -1,   -1,   -1,   -1,   -1,    0,   -1,    0,   -1,   -1 ],
  [ -1,   -1,   -1,   -1,    0,   -1,    0,   -1,   -1,   -1 ],
  [ -1,   -1,   -1,    0,   -1,    0,   -1,   -1,   -1,    0 ],
  [ -1,   -1,   -1,   -1,    0,   -1,   -1,   -1,    0,   -1 ],
  [  0,   -1,   -1,   -1,   -1,   -1,   -1,    0,   -1,    0 ],
  [ -1,   -1,   -1,   -1,   -1,   -1,    0,   -1,    0,   -1 ]

], dtype=np.float32)

room_number = { (0,0): 0, (0,1): 1, (0,8): 8, (1,0): 0, (1,2): 2, (2,1): 1, (2,3): 3, 
                (3,2): 2, (3,6): 6, (4,5): 5, (4,7): 7, (5,4): 4, (5,6): 6, (6,3): 3, 
                (6,5): 5, (6,9): 9, (7,4): 4, (7,8): 8, (8,0): 0, (8,7): 7, (8,9): 9, 
                (9,6): 6, (9,8): 8 } 

Rroom_number = { (0,0): (0,0), (0,1): (1,0), (0,8): (3,1), (1,0): (0,0), (1,2): (1,1), (2,1): (1,0), (2,3): (1,2), 
                 (3,2): (1,1), (3,6): (2,2), (4,5): (2,1), (4,7): (3,0), (5,4): (2,0), (5,6): (2,2), (6,3): (1,2), 
                 (6,5): (2,1), (6,9): (3,2), (7,4): (2,0), (7,8): (3,1), (8,0): (4,1), (8,7): (3,0), (8,9): (3,2), 
                 (9,6): (2,2), (9,8): (3,1) } 
                


targets = [(0,0), (1,0), (8,0)]
#print(Q, '\n','\n', R)

points = [(0,0), (0,1), (0,8), (1,2), (2,3), (3,6),
          (4,5), (4,7), (5,6), (6,9), (7,8), (8,9)]

plt.figure(figsize=(12,8))
G=nx.Graph()
G.add_edges_from(points)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)
plt.show()

def updateQ(Q, R, row, column):
  all_possible_moves = np.argwhere(R[column] != -1).T[0]
  Qpos_values = []
  for index in all_possible_moves:
    Qpos_values.append(R[column, index])

  Qpos_values = np.array(Qpos_values)
  Q[row, column] = R[row, column] + GAMMA * np.amax(Qpos_values)
  
  return Q
  
def init(R, in_state, targets):                                                             
  row = in_state
  if np.amax(R[row]) != 0 and np.amax(R[row]) != -1:
    max_value_index = np.argwhere(R[row] == np.amax(R[row])).T[0]
    random_ch = np.random.randint(max_value_index.shape[0])
    max_value_index = max_value_index[random_ch]
    column = max_value_index
  else:
    max_value_index = np.argwhere(R[row] != -1).T[0]
    random_ch = np.random.randint(max_value_index.shape[0])
    max_value_index = max_value_index[random_ch]
    column = max_value_index                                                                                                                                                 

  if (targets is not None) and (len(targets) != 0):
    for target in targets:
      if target == (row, column):
        R[row, column] = 100
        targets = targets.remove(target)
                                                                                   
  return row, column, R, targets

def check(R, row, column, trg):
  for target in trg:
    if target == (row, column):
      return True
  return False

def train(R, Q, targets, epochs):
  h_targets = [(0,0), (1,0), (8,0)]
  for _ in range(epochs):
    in_state = np.random.randint(ROWS)
    flag = False
    while flag == False:
      row, column, R, targets = init(R, in_state, targets)
      Q = updateQ(Q, R, row, column)
      in_state = column
      flag = check(R, row, column, h_targets)
    
    for i in range(ROWS):
      for j in range(COLS):
        if R[i][j] != -1:
          R[i][j] = Q[i][j]

  return R, Q, targets

def query(R, Q, targets):
  h_targets = [(0,0), (1,0), (8,0)]
  in_state = np.random.randint(ROWS)
  flag = False
  agent_muhtar = []
  while flag == False:
    row, column, R, targets = init(R, in_state, targets)
    agent_muhtar.append((row, column))  

    Q = updateQ(Q, R, row, column)
    in_state = column
    flag = check(R, row, column, h_targets)
  
  for i in range(ROWS):
    for j in range(COLS):
      if R[i][j] != -1:
        R[i][j] = Q[i][j]

  return R, Q, agent_muhtar

R, Q, targets = train(R, Q, targets, 20)

set_option("display.precision", 2)
# np.set_printoptions(precision=2)
print(DataFrame(R))
print('\n')
print(DataFrame(Q))
print('\n')

R, Q, agent_muhtar = query(R, Q, targets)

tmp = []

for elem in agent_muhtar:
  for key in room_number:
    if elem == key:
      tmp.append(key)
      print(f'Мухтар пішов у кімнату номер: {room_number[key]}')


lst = []

for elem in tmp:
  for key in Rroom_number:
    if elem == key:
      lst.append(Rroom_number[key])
  

set_option("display.precision", 2)
print('\n', '\n')
print(DataFrame(R))
print('\n', '\n')
print(DataFrame(Q))


visualization.main(lst)

