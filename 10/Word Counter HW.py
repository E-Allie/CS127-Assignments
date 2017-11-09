def remove_non_alpha(w):
    """
    input: w is a string representing a word (or a string of the entire text)
    output: the word (or text) with only alpha-chars (spaces) and apostrophes
    """
    
    w=list(w)
    for i,l in enumerate(w):
        if not l.isalpha() and l!="'" and l!=" " and l!="\n":
            w[i]=""
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
        d.setdefault(w,[])
        if i<len(tl)-1:
            d[w].append(tl[i+1])
    return d

d=build_word_sequence("hamlet.txt")
print(d)

"""
d=build_word_sequence("psalms.txt")
open("psalms words.txt","w+").write(str(d))
Some text editors struggle with that.
"""