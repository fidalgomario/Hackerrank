n, m = map(int, input().split())
table = [1] * (m - n + 1)
if n == 1:
    table[0] = 0
for i in range(2, 40000):
    for j in range(max(i * i, (n + i - 1) // i * i), m // i * i + 1, i):
        table[j - n] = 0;
print(len([i for i in range(m - n + 1 - 2) if table[i] and table[i + 2]]))
