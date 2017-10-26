def people(A,B,u):
    unitp=A/B
    amountp=u/unitp
    return int(amountp)

print((people(5,10,1)))
print((people(10,5,8)))
print((people(20,4,50)))