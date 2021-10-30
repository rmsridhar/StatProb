def recursion(n):

    if (n==1):
        return 1
    else:
        return (n*recursion(n-1))

print(recursion(3))
