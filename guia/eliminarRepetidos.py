import re

def sacarIguales(sA,sB):
    for eachChar in sA:
        if(eachChar in sB):
            sB = re.sub(eachChar,"",sB , count = 1)
            sA = re.sub(eachChar,"",sA , count = 1)
    return sA, sB
