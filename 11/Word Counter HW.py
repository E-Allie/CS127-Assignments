import random

def remove_non_alpha(w):
    """
    input: w is a string representing a word (or a string of the entire text)
    output: the word (or text) with only alpha-chars (spaces) and apostrophes
    """
    
    w=list(w)
    i=0
    for i,l in enumerate(w):
        if not l.isalpha() and l!="\'" and l!=" " and l!="\n":
                w[i]=" "
    w="".join(w)
    return w

def build_word_sequence(f):
    """
    input: f - string representing filename
    output: a dictionary with keys of words and values of list of following words
    """
    text = open(f).read()
    tl=list(remove_non_alpha(text.lower().replace("-"," ")).split())
    d={}
    for i,w in enumerate(tl):
        if i<len(tl)-1:
            d.setdefault((tl[i],tl[i+1]),[])
        if i<len(tl)-2:
            d[(tl[i],tl[i+1])].append(tl[i+2])
    """
    Remove if not for human consumption.
    for w in d:
        d[w].sort()
    """
    return d

def generate_text(d,next1,length=50):
    wordlist=[]
    for i in next1:
        wordlist.append(i)
    for i in range(length):
        if next1 not in d:
            break
        next=(next1[1],random.choice(d[next1]))
        wordlist.append(next[1])
        next1=(next1[1],next[1])
    wordlist=" ".join(wordlist)
    return wordlist

d=build_word_sequence("psalms.txt")
print(generate_text(d,("o","lord"),50))


"""
d=build_word_sequence("psalms.txt")
open("psalms words.txt","w+").write(str(d))
Some text editors struggle with that.
"""