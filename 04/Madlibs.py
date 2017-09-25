import random as r

initstory = """
There once was a(n) NOUN who lived in a(n) NOUN . NAME PASTTENSEVERB to VERB .
NAME PASTTENSEVERB a(n) NOUN , they felt ADJECTIVE about this . PRONOUN lived ADVERB 
 ever after .
"""

finstory=""
name=""
nounlist=["couch", "dog", "foot", "aardvark", "candy", "pirate", "eagle", "table", "chair", "house", "World Eater"]
verblist=["jump","eat","attacc","protecc","ride","smash","meme","slay"]
ptverblist=['jumped','ate','killed','attacced','proteccted','rode','smashed','memed','slayed','roared']
adverblist=['amazingly']
adjlist=['glorious']
namelist=['Christopher Walken']
pronounlist=['They']

story = initstory.split()

for i in story:
    if "PRONOUN" in i:
        i = pronounlist[r.randrange(len(pronounlist))]
        finstory += " "+ i
    elif "PASTTENSEVERB" in i:
        i= ptverblist[r.randrange(len(ptverblist))]
        finstory += " "+i
    elif "ADVERB" in i:
        i = adverblist[r.randrange(len(adverblist))]
        finstory += " "+i
    elif "ADJECTIVE" in i:
        i = adjlist[r.randrange(len(adjlist))]
        finstory += " "+i
    elif "VERB" in i:
        i = verblist[r.randrange(len(verblist))]
        finstory += " "+i
    elif "NOUN" in i:
        i = nounlist[r.randrange(len(nounlist))]
        finstory += " "+i
    elif "NAME" in i:
        if name != "":
            i = name
            finstory += " "+i
        else:
            i = namelist[r.randrange(len(namelist))]
            name=i
            finstory += " "+i
    elif "," in i:
        finstory += ","
    elif "." in i:
        finstory += "."
    else:
        finstory += " "+i
            

print(finstory)
