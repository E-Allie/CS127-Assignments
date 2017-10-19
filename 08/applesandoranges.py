def trees(hstart,hend,atree,btree,apples,bapples,dapp,dbapp):
    happ=0
    hbapp=0
    
    for i in range(apples):
        if hstart<=atree+dapp[i]<=hend:
            happ+=1
    for i in range(bapples):
        if hstart<=btree+dbapp[i]<=hend:
            hbapp+=1
    return(str(happ)+"\n"+str(hbapp))


fruits=open("fruitsimport").read().splitlines()
s,t=fruits[0].split(" ")
a,b=fruits[1].split(" ")
m,n=fruits[2].split(" ")
da=[]
do=[]
for i in fruits[3].split(" "):
    da.append(int(i))
for i in fruits[4].split(" "):
    do.append(int(i))

s,t,a,b,m,n=int(s),int(t),int(a),int(b),int(m),int(n)

print(trees(s,t,a,b,m,n,da,do))