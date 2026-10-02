from random import sample, random

N = 100

OBJECTS = [n for n in range(N)]
SETS = [set(sample(OBJECTS, s+1)) for s in range(N)]
COSTS = [10*random()+(s*random())**2 for s in range(N)]

print(SETS)
print(COSTS)