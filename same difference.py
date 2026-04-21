from collections import defaultdict
t=int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = defaultdict(int)
    for i in range(n):
        key = a[i] - i
        freq[key] += 1
    ans = 0
    for f in freq.values():
        ans += f * (f - 1) // 2
    print(ans)
