We try to solve a subset of the min weighted max independent set problem. The files in the folder are described as follows:

+ solver\_ILP
    This file has a Gurobi Program to run a constrained optimization problem with binary switch varibles.  These represent the inclusion/ommision of vertices in the solution independent set.
    
+ solver_LP
    The binary switch varibles are relaxed to be in \[0,1\].
    
+ input.data
    This represents a small problem instance.

++ Graph:

```

    ---------
    | ------|-
    | |      |
    3 5     3 5
          /
         /
        /
    4 2     4 2
    | |     | |
    --|------ |
      ---------
```

++ File:

```
<#agents>
w(<C1[v][1]>) ... w(<C2[v][k_1])
...
<#conflicts>
agent1 path1 agent2 path2
```

P.S. - In case you have never used Gurobi before, you can checkout the "setupGurobi" folder in my [utilities repo](https://github.com/sailik1991/utilities).
