def caught_speeding(speed, is_birthday):
    if is_birthday==True:
        if speed>=66 and speed<=85:
            return 1
        elif speed>=86:
            return 2
        else:
            return 0
    else:
        if speed>=61 and speed<=80:
            return 1
        elif speed>=81:
            return 2
        else:
            return 0