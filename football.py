n=int(input())
dict1={}
for i in range(n):
    s=input()
    if s in dict1:
        dict1[s]+=1
    else:
        dict1[s]=1
result = max(dict1, key=dict1.get)
print(result)
