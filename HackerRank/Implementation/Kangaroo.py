def kangaroo(x1, v1, x2, v2):
    if(x1 < x2 and v1 < v2):
        return("NO")
    if(v2-v1==0 and x2-x1==0):
        return("YES")
    if(v2-v1==0 and x2!=x1):
        return("NO")
    if((x1-x2)%(v2-v1)==0):
        return("YES")
    else:
        return("NO")