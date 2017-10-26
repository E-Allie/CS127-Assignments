def encode(s):
    final=[]
    amount=1
    single=0
    for i,l in enumerate(s):
        if i==0 and len(s)>1:
            if l!=s[1]:
                final.append(l)
                single=1
        elif 0<i<len(s)-1:
            if single==0:
                if l==s[i-1]:
                    amount+=1
                elif l!=s[i+1] and l!=s[i-1]:
                    final.append(amount)
                    final.append(s[i-1])
                    final.append(l)
                    amount=1
                    single=1
                else:
                    final.append(amount)
                    final.append(s[i-1])
                    amount=1
            elif single==1:
                if l!=s[i-1] and l!=s[i+1]:
                    final.append(l)
                else:
                    single=0
    else:
        if single==1:
            final.append(l)
        elif l!=s[i-1]:
            final.append(amount)
            final.append(s[i-1])
            final.append(l)
        elif len(s)>1:
            amount+=1
            final.append(amount)
            final.append(l)
        else:
            final.append(l)
    return final

print(encode("baabbbcrddeeee"))
print(encode("aabbbcrddeeekesr"))
print(encode("abcdefg"))
print(encode("a"))
print(encode("ab"))
print(encode("aa"))
print(encode("aba"))
