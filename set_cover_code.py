# Set Cover Problem - Greedy Approximation (Python)
def greedy_set_cover(universe, subsets):
    covered = set()
    cover = []
    while covered != universe:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset
    return cover

universe = set(range(1, 7))
subsets = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5, 6}]
print(greedy_set_cover(universe, subsets))

