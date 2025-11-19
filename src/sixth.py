def find_pairs(lst, target):
    pairs = []
    seen = set()

    for num in lst:
        complement = target - num
        if complement in lst and (min(num, complement), max(num, complement)) not in seen:
# Avoid duplicates and count each pair only once
            pairs.append((num, complement))
            seen.add((min(num, complement), max(num, complement)))
    return pairs

# Example input
numbers = [2, 4, 3, 5, 7, 8, -1]
target = 6

result = find_pairs(numbers, target)
print(result)  # Output: [(2, 4), (3, 3), (7, -1)]