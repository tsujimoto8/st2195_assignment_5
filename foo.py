
def is_divisible_by_k(x, k):
    # Checks whether x is divisible by k.
    return x%k == 0

# Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
x = []
for i in range(1,1001):
    if (is_divisible_by_k(i, 2) | is_divisible_by_k(i, 5)) | is_divisible_by_k(i, 7):
        x.append(i)

# Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
print(sum(x))