lower = input()
lower = lower.partition(" ")
namea = lower[0]
nameb = lower[2]
upper = namea.capitalize()+" "+nameb.capitalize()
print(upper)