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
        if unhappy(board):
            return("NO")
    return("YES")

def unhappy(bugs):
    if len(bugs)==2:
        if bugs[0]!=bugs[1]:
            return True
        else:
            return False
    for i, bug in enumerate(bugs):
        if i == 0 or i == len(bugs)-1:
            continue
        if bug!=bugs[i+1] and bug!=bugs[i-1]:
            return True


"""games=open("bugsimport").read().splitlines()
for i in games:
    z=i.replace("_","")
    if z.isalpha()==True:
        print(buglist(i))
"""

g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    b = input().strip()
    print(buglist(b))
    
#Hackerrank tested, hacker approved!

