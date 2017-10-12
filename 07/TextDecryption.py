import math as m

proto={}
dists=[]

def encode_letter(letter,amount):
    initval=ord(letter)
    #coterminal amounts
    if amount>26:
        while amount>26:
            amount-=26
    newval=initval+amount
    if (90>=initval and newval>90) or newval>122:
        newval-=26
    newletter=chr(newval)
    return newletter

def encode_string(string, amount):
    raw=list(string)
    newrawstr=[]
    while len(raw)>0:
        char=raw.pop(0)
        if char.isalpha():
            newrawstr.append(encode_letter(char,amount))
        else:
            newrawstr.append(char)
    newstr="".join(newrawstr)
    return newstr

def full_encode(string):
    fullarr=[]
    for i in range(26):
        fullarr.append(encode_string(string,i))
    return fullarr

def decode(encytd):
    global dists
    setletters()
    fullarr=full_encode(encytd)
    barr=list(fullarr)
    x=-1
    for strong in barr:
        x+=1
        for i in strong:
            if i.isalpha()==False:
                strong=strong.replace(i,"")
                barr[x]=strong
    checker(barr)
    rot=dists.index(min(dists))
    dists=[]
    return(fullarr[rot:rot+1])

def setletters():
    global proto
    total=0
    arch={}
    book = open("import.txt").read()
    book=book.lower()
    for c in book:
        if c.isalpha()==False:
            book=book.replace(c,"")
    for c in book:
        total+=1
        if c in arch:
            arch[c]+=1
        else:
            arch[c]=1
    for key in arch:
        proto[key]=(arch[key]/total)*100

def checker(arrays):
    array=list(arrays)
    for i in range(len(array)):
        letfreq={}
        test=array.pop(0)
        test=test.lower()
        for character in test:
            letfreq.setdefault(character,(test.count(character)/len(test))*100)
        distance(letfreq)
      
def distance(let):
    #letfreq
    global dists
    global proto
    inrtsum=0
    for i in let:
        inrtsum+=(proto[i]-let[i])**2
    dists.append(m.sqrt(inrtsum))


print(decode("Mabl bl t mxlm."))
print("Some phrases do not work.")
print(decode("Jfdv gyirjvj ufe'k nfib."))
print("I hope you like Shakespeare.")
print(decode("Jul, gurer'f ab erzrql; 'gvf gur phefr bs freivpr, Cersrezrag tbrf ol yrggre naq"))
print(decode("F tlria ilsb ql exsb xklqebo tlohfkd qbpq"))
print(decode("""
Abpmfpb jb, fc F al klq. Qeobb dobxq lkbp lc qeb zfqv,
Fk mboplkxi prfq ql jxhb jb efp ifbrqbkxkq,
Lcc-zxmm'a ql efj: xka, yv qeb cxfqe lc jxk,
F hklt jv mofzb, F xj tloqe kl tlopb x mixzb:
Yrq eb; xp ilsfkd efp ltk mofab xka mromlpbp,
Bsxabp qebj, tfqe x yljyxpq zfozrjpqxkzb
Eloofyiv pqrcc'a tfqe bmfqebqp lc txo;
Xka, fk zlkzirpflk,
Klkprfqp jv jbafxqlop; clo, 'Zboqbp,' pxvp eb,
'F exsb xiobxav zelpb jv lccfzbo.'
Xka texq txp eb?
Clopllqe, x dobxq xofqejbqfzfxk,
Lkb Jfzexbi Zxppfl, x Cilobkqfkb,
X cbiilt xijlpq axjk'a fk x cxfo tfcb;
Qexq kbsbo pbq x pnrxaolk fk qeb cfbia,
Klo qeb afsfpflk lc x yxqqib hkltp
Jlob qexk x pmfkpqbo; rkibpp qeb yllhfpe qeblofz,
Tebobfk qeb qldba zlkprip zxk molmlpb
Xp jxpqboiv xp eb: jbob moxqqib, tfqelrq moxzqfpb,
Fp xii efp pliafbopefm. Yrq eb, pfo, exa qeb bibzqflk:
Xka F, lc telj efp bvbp exa pbbk qeb mollc
Xq Oelabp, xq Zvmorp xka lk lqebo dolrkap
Zeofpqfxk xka ebxqebk, jrpq yb yb-ibb'a xka zxij'a
Yv abyfqlo xka zobafqlo: qefp zlrkqbo-zxpqbo,
Eb, fk dlla qfjb, jrpq efp ifbrqbkxkq yb,
Xka F--Dla yibpp qeb jxoh!--efp Jllopefm'p xkzfbkq."""))