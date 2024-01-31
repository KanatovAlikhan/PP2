import itertools
def perm():
    for x in permutations:
        print(x)
s=str(input())
permutations = list(itertools.permutations(s))
perm()