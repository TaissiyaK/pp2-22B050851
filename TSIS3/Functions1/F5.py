import itertools
string = input()
elements = list(string)
permutation_in_string = list(itertools.permutations(elements))
print([''.join(permutation_in_string) for permutation_in_string in permutation_in_string])