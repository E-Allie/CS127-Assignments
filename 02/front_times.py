def front_times(str, n):
    str3=str[0:3]
    strinit=str3
    if n>0:
        for x in range(n-1):
          str3=str3+strinit
        return str3
    else:
        return ""