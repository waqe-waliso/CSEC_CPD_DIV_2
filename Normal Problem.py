t=int(input())
for _ in range(t):
    ans=""
    a=input()
    for v in a[::-1]:
        if v=="q":
            ans+="p"
        elif v=="w":
            ans+="w"
        elif v=="p":
            ans+="q"
    print(ans)
