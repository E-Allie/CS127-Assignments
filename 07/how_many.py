def freq(num,list):
    r=0
    for x in list:
        if x==num:
            r+=1
    return(r)

def min(list):
    r=list[1]
    for x in list:
        if r>x:
            r=x
    return(r)

def mode(list):
    modez={0:0}
    curr=0
    for x in list:
        if freq(x,list)>modez[curr]:
            curr=x
            modez[curr]=freq(curr,list)        
    return(curr)

print(freq(2,[3,2,2,1,3,4,5,4,3,4,3,4,4]))
print(min([3,2,2,1,3,4,5,4,3,4,3,4,4]))
print(mode([3,2,2,1,3,4,5,4,3,4,3,4,4,4]))