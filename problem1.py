s = input().strip()
n = len(s)

t = s + s   # cyclic handling

char_set = set()
l = 0
current_sum = 0
max_sum = 0

def value(c):
    return ord(c) - ord('a') + 1

for r in range(len(t)):
    while t[r] in char_set:
        char_set.remove(t[l])
        current_sum -= value(t[l])
        l += 1

    char_set.add(t[r])
    current_sum += value(t[r])

    # window length should not exceed original string
    while (r - l + 1) > n:
        char_set.remove(t[l])
        current_sum -= value(t[l])
        l += 1

    max_sum = max(max_sum, current_sum)

print(max_sum)
