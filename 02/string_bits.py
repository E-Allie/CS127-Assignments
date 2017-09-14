def string_bits(str):
    altstr=""
    i=1
    while i<len(str)+1:
        altstr=altstr+str[i-1:i]
        i=i+2
    return altstr