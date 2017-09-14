def string_times(str, n):
    strinit=str
    if n>0:
        for x in range(n-1):
          str=str+strinit
        return str
    else:
        return ""