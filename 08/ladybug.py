def freq(num,list):
    r=0
    for x in list:
        if x==num:
            r+=1
    return(r)

def buglist(b):
    board=list(b)
    for i, bug in enumerate(board):
        if bug.isalpha()==True:
            if freq(bug,board)<=1:
                return("NO")
    if "_" not in board:
        x=happy(board)
        if x==1:
            return("NO")
    return("YES")

def happy(bugs):
    for i, bug in enumerate(bugs):
        if i == 0 or i == len(bugs)-1:
            continue
        if bug!=bugs[i+1] and bug!=bugs[i-1]:
            return(1)


games=open("bugsimport").read().splitlines()
for i in games:
    z=i.replace("_","")
    if z.isalpha()==True:
        print(buglist(i))

