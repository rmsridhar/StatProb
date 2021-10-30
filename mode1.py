def mode(data):
    lst =[]
    hgh=0
    for i in range(len(data)):
        lst.append(data.count(data[i]))
    print(lst)
    m= max(lst)
    ml = [x for x in data if data.count(x)==m ] #to find most frequent values
    mode = []
    for x in ml: #to remove duplicates of mode
        if x not in mode:
            mode.append(x)
    return mode
print (mode([1,2,2,2,2,7,7,5,5,5,5]))
