lst="123"
for i in range(len(lst)):
    m=lst[i]
    print(m)
    r=lst[:i]+lst[i+1:]
    print(r)
