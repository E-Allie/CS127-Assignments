

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

print(full_encode("""
Despise me, if I do not. Three great ones of the city,
In personal suit to make me his lieutenant,
Off-capp'd to him: and, by the faith of man,
I know my price, I am worth no worse a place:
But he; as loving his own pride and purposes,
Evades them, with a bombast circumstance
Horribly stuff'd with epithets of war;
And, in conclusion,
Nonsuits my mediators; for, 'Certes,' says he,
'I have already chose my officer.'
And what was he?
Forsooth, a great arithmetician,
One Michael Cassio, a Florentine,
A fellow almost damn'd in a fair wife;
That never set a squadron in the field,
Nor the division of a battle knows
More than a spinster; unless the bookish theoric,
Wherein the toged consuls can propose
As masterly as he: mere prattle, without practise,
Is all his soldiership. But he, sir, had the election:
And I, of whom his eyes had seen the proof
At Rhodes, at Cyprus and on other grounds
Christian and heathen, must be be-lee'd and calm'd
By debitor and creditor: this counter-caster,
He, in good time, must his lieutenant be,
And I--God bless the mark!--his Moorship's ancient.

I would love to have another working test
"""))
    