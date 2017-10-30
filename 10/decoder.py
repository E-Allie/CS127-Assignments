def rle_decode(e):
    f=""
    i=0
    while i<len(e):
        n=e[i]
        if type(n)==str:
            f+=n
            i+=1
        else:
            f+=n*e[i+1]
            i+=2
    return f

print(rle_decode([4,"a",3,"b","c"]))