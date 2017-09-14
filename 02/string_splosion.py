def string_splosion(str):
    altstr=""
    i=1
    while i<len(str)+1:
        altstr=altstr+str[0:i]
        i=i+1
    return altstr