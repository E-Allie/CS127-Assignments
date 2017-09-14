def lone_sum(a, b, c):
    sum=0
    if a==b==c:
        sum=0
    elif a==b:
        sum=c
    elif a==c:
        sum=b
    elif b==c:
        sum=a
    else:
        sum=a+b+c
    return sum