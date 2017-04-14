```
$> gurobi.sh solver_ILP.py input.data  
Adding constraint: 0:2 1:0
Adding constraint: 0:0 1:0
Adding constraint: 0:1 1:1
Adding constraint: 0:2 1:2
Adding constraint: 0:3 1:3
Optimize a model with 7 rows, 8 columns and 18 nonzeros
Variable types: 0 continuous, 8 integer (0 binary)
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [2e+00, 5e+00]
  Bounds range     [1e+00, 1e+00]
  RHS range        [1e+00, 1e+00]
Presolve removed 7 rows and 8 columns
Presolve time: 0.00s
Presolve: All rows and columns removed

Explored 0 nodes (0 simplex iterations) in 0.00 seconds
Thread count was 1 (of 12 available processors)

Solution count 1: 5 
Pool objective bound 5

Optimal solution found (tolerance 1.00e-04)
Best objective 5.000000000000e+00, best bound 5.000000000000e+00, gap 0.0000%
---------------
x-0-0 -> 1
x-0-1 -> 0
x-0-2 -> 0
x-0-3 -> 0
x-1-0 -> 0
x-1-1 -> 0
x-1-2 -> 1
x-1-3 -> 0
---------------
Obj -> 5
---------------
```

```
$>  gurobi.sh solver_LP.py input.data 
Adding constraint: 0:2 1:0
Adding constraint: 0:0 1:0
Adding constraint: 0:1 1:1
Adding constraint: 0:2 1:2
Adding constraint: 0:3 1:3
Optimize a model with 7 rows, 8 columns and 18 nonzeros
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [2e+00, 5e+00]
  Bounds range     [1e+00, 1e+00]
  RHS range        [1e+00, 1e+00]
Presolve time: 0.00s
Presolved: 7 rows, 8 columns, 18 nonzeros

Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    4.0000000e+00   1.000000e+00   0.000000e+00      0s
       1    5.0000000e+00   0.000000e+00   0.000000e+00      0s

Solved in 1 iterations and 0.00 seconds
Optimal objective  5.000000000e+00
---------------
x-0-0 -> 1
x-0-1 -> 0
x-0-2 -> 0
x-0-3 -> 0
x-1-0 -> 0
x-1-1 -> 0
x-1-2 -> 1
x-1-3 -> 0
---------------
Obj -> 5
---------------
```
