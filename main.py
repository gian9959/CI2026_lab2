from random import sample, random, seed

MAX_RETRY = 1000

N = 20
seed(42)

def fitness(sol):
    weight = sum(s["cost"] for s in sol)
    check = set()
    for s in sol:
        for e in s["elements"]:
            check.add(e)
    assert check == set(range(N))
    return -weight

def tweak(sol):
    check = set()
    retry = 0
    n_sol = sol
    while check != set(range(N)):
        if retry > MAX_RETRY:
            return sol

        retry += 1
        n_sol = sample(sol, len(sol)-1)

        check.clear()
        for s in n_sol:
            for e in s["elements"]:
                check.add(e)

    return n_sol

SETS = [
    {
        "elements": set(sample(range(N), s+1)),
        "cost": 10*random()+(s*random())**2,
    } for s in range(N)
]
solution = [SETS[i] for i in range(N)]
for i in range(1000):
    new_solution = tweak(solution)
    new_fitness = fitness(new_solution)
    if new_fitness > fitness(solution):
        solution = new_solution
        print(f"SOLUTION {i}:")
        print(new_solution)
        print(f"WEIGHT: {new_fitness}")
        print()