# Water Jug Problem using BFS and DFS

## Problem Description

We are given two jugs:

- Jug1 capacity = 4 litres  
- Jug2 capacity = 3 litres  

The goal is to measure exactly **2 litres** of water.

Initial State: (0, 0)  
Goal Condition: Either jug contains 2 litres.

---

## State Representation

A state is represented as:

(x, y)

Where:
- x = water in Jug1
- y = water in Jug2

Example:
(4, 2) means Jug1 has 4 litres and Jug2 has 2 litres.

---

## Actions

From any state, the following actions are possible:

- Fill Jug1
- Fill Jug2
- Empty Jug1
- Empty Jug2
- Pour water from Jug1 → Jug2
- Pour water from Jug2 → Jug1

These actions generate new states in the state space.

---

## Search Algorithms Used

### Breadth First Search (BFS)

- Uses a Queue (FIFO – First In First Out)
- Explores the state space level by level
- Complete (always finds a solution if it exists)
- Guarantees the shortest path (optimal solution)

### Depth First Search (DFS)

- Uses a Stack (LIFO – Last In First Out)
- Explores deep into one branch before backtracking
- May not always give the shortest solution
- Uses less memory compared to BFS

---

## State Space Representation

The Water Jug problem can be represented as a graph:

- Nodes = States (x, y)
- Edges = Actions (Fill, Empty, Pour)
- Initial Node = (0, 0)
- Goal Node = Any state where x = 2 or y = 2

---

## Performance Comparison

BFS:
- Complete 
- Optimal 
- Higher memory usage 

DFS:
- Not always optimal 
- Uses less memory 
- Can go deep into search tree

In this implementation, both BFS and DFS found the solution path:

(0, 0)  
(0, 3)  
(3, 0)  
(3, 3)  
(4, 2)

---

## Sample Output
