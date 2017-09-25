coms=["Dogs","don't","like","cats"]
other=["1","2","1","2","3","4"]

def comma(lyst):
    statement=""
    for i in lyst:
        if i not in lyst[:len(lyst)-1]:
            statement+=i+"."
        elif i not in lyst[:len(lyst)-2]:
            statement+=i+", and "
        else:
            statement+=i+", "
    print(statement)
    return statement

comma(coms)
comma(other)