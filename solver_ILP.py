#!/usr/bin/python

#   minimize 
#       Sum x[v] * w[v]
#   subject to
#       For each C, Sum x[v] = 1
#       For each conflict edge (u,v), x[u] + x[v] <= 1
#       x[v] is binary

from gurobipy import *

# Create a model
m = Model("ILP")

# Input problem file (detail in README.md)
f = open(sys.argv[1], 'r')

# Add objective function and clique constraint to model 
agents = int(f.readline())
obj = LinExpr()
X = []
for i in range(agents):
    x = []
    cliqueConstr = LinExpr()
    w = map(int, f.readline().split("|"))
    for j in range(len(w)):
        n = "x-{0}-{1}".format(i,j)
        x.append(m.addVar(lb=0, ub=1, vtype=GRB.INTEGER, name=n))
        cliqueConstr.add( x[j] )
        obj.add( x[j], w[j])
    m.addConstr( cliqueConstr == 1 )
    X.append(x)
m.update()

# Add inter-clique conflict constrainst to model
conflicts = int(f.readline())
for i in range(conflicts):
    edgeConstr = LinExpr()
    c1, v1, c2, v2 = map(int, f.readline().split("|"))
    # Intra clique conflicts handled in clique constraints
    if c1 != c2:
        print( "Adding constraint: {0}:{1} {2}:{3}".format(c1, v1, c2, v2) )
        edgeConstr.add( X[c1][v1] )
        edgeConstr.add( X[c2][v2] )
        m.addConstr( edgeConstr <= 1 )

m.setObjective(obj, GRB.MINIMIZE)
m.optimize()

try:
    print ('---------------')
    for v in m.getVars():
        print('%s -> %g' % (v.varName, v.x))
        #print('%s' % (v.varName))

    print ('---------------')
    print('Obj -> %g' % m.objVal)
    print ('---------------')
except:
    # If exception occurs- couldn't find variables to print.
    # Thus, model was infeisable.
    m.computeIIS()
    m.write("model.ilp")
