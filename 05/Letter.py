

def encode_letter(letter, amount):
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

print(encode_letter("A",133), encode_letter("c",14), encode_letter("r",17))
