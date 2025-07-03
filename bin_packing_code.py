# Bin Packing Problem - First Fit Decreasing (Python)
def bin_packing(items, bin_size):
    bins = []
    for item in sorted(items, reverse=True):
        placed = False
        for b in bins:
            if sum(b) + item <= bin_size:
                b.append(item)
                placed = True
                break
        if not placed:
            bins.append([item])
    return bins

print(bin_packing([4, 8, 1, 4, 2, 1], 10))
