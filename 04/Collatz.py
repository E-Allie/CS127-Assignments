def collatz():
    global inp
    if inp%2==0:
        inp=inp/2
    else:
        inp=inp*3+1
    print (inp)
    
inp=input()

try:
    inp=int(inp)
except:
    print("Please input an integer value.")

if type(inp) is int:
    while inp!=1:
        collatz()