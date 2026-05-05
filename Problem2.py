n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# Step 1: Check feasibility
mod = arr[0] % k
for x in arr:
    if x % k != mod:
        print(-1)
        exit()

# Step 2: Sort array
arr.sort()

# Step 3: Choose median
target = arr[n // 2]

# Step 4: Calculate operations
operations = 0
for x in arr:
    operations += abs(x - target) // k

print(operations)
