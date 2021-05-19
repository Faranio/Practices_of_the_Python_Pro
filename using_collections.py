import collections


def most_frequent(numbers):
    counts = collections.Counter(numbers)
    return max(counts, key=lambda x: counts[x])


result = most_frequent([2, 2, 3, 4, 1, 4, 5, 3, 5, 6, 2, 5, 2, 3, 1, 6, 7, 8, 5, 4, 6, 7, 5, 6])
print(result)
