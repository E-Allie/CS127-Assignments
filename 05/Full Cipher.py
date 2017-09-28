

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
    fullstr=""
    for i in range(1,26):
        fullstr+=encode_string(string,i)+"\n"
    return fullstr

print(full_encode("Hello!"))
    