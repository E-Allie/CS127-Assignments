def piglatin(init):
    if init[0] in "aeiouAEIOU":
        return init+"ay"
    else:
        return init[1:len(init)]+init[0]+"ay"
        
print(piglatin("hello"))
print(piglatin("test"))
print(piglatin("Excellent"))