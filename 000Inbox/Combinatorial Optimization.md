---
tags:
  - business-data-science
---
# Combinatorial Optimization

- Reference:

   - SLide: [Introduction to Combinatorial Optimization](https://rtime.ciirc.cvut.cz/\~hanzalek/KO/Basic_e.pdf)

   - Course: [Discrete Optimization](https://www.coursera.org/learn/discrete-optimization)

   - Tool: [Google OR-TOOLs](https://developers.google.com/optimization)

      - [Getting the value of variables created during the search at solution](https://github.com/google/or-tools/issues/628)

      - [ortools.sat.python.cp_model](http://google.github.io/or-tools/python/ortools/sat/python/cp_model.html#LinearExpr.GetIntegerVarValueMap)

   - [Modelling graph coloring with integer linear programming](https://manas.tech/blog/2010/09/16/modelling-graph-coloring-with-integer-linear-programming/)

   - Heuristic algorithm

   - [A quick heuristic for combinatorial optimization using Python Numba and GPU](https://jcrousse.medium.com/a-quick-heuristic-for-combinatorial-optimization-using-python-numba-and-gpu-a88505ad4e6e)

- Combinatorial optimization is a subfield of mathematical optimization that consists of finding an optimal object from a finite set of objects, where the set of feasible solutions is discrete or can be reduced to a discrete set. 

- Characteristics of Combinatorial Optimization Problem

   - They usually require clustering, sorting, or assigning a set of discrete objects fulfilling some constraints

   - It relatively easy to assess an individual solution

   - They are very complex computationally

      - \[\[NP-Hard\]\]

      - Some general algorithm are often inefficient or impossible to use ( Dynamic programming, branch and bound ... )

      - Find a near-optimal solution in a reasonable time is a valid option

- Typical combinatorial optimization problems

   - travelling salesman problem (TSP)

   - minimum spanning tree problem (MST)

      - 應用: 線路設計，例如沿著街道(邊)為住家(節點)架設電纜的情境、成本最低的路徑

   - knapsack problem

- Optimization Paradigms in discrete optimization (範式、典範、策略)

   - \[\[Constraint Programming\]\] (CP)

      - It is characterized by two key ideas: 

         - To express the optimization problem at a high level to reveal its structure

         - To use constraints to reduce the search space by removing, from the variable domains, values that cannot appear in solutions

      - Constraint programming is an optimization technique that emerged from the field of artificial intelligence

   - Local Search (LS)

      - It consists in starting from a solution and improving it by performing (typically) local perturbations (often called moves)

      - Local search is probably the oldest and most intuitive optimization technique. Local search has evolved substantially in the last decades with a lot of attention being devoted on which moves to explore. 

      - Include the concept of neighborhood and connectivity to meta-heuristics such as tabu search and simulated annealing.

   - Linear Programming (LP)

      - Linear programming has been, and remains, a workhorse of optimization.

      - It consists in optimizing a linear objective subject to linear constraints, admits efficient algorithmic solutions, and is often an important building block for other optimization techniques.

      - These lectures review fundamental concepts in linear programming, including the infamous simplex algorithm, simplex tableau, and duality. 

   - Mixed Integer Programming (MIP)

      - Mixed Integer Programming generalizes linear programming by allowing integer variables, which dramatically changes the complexity of the problems but also broadens the potential applications significantly. These lectures review how to model problems in mixed-integer programming and how to solve mixed-integer programs using branch and bound. Advanced techniques such as cutting planes and polyhedral cuts are also covered.