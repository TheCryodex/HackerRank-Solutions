def countApplesAndOranges(s, t, a, b, apples, oranges):
    resapp=[]
    capp=0
    resor=[]
    cor=0
    for i in apples:
        resapp.append(a+i)
    for i in oranges:
        resor.append(b+i)
    for i in resapp:
        if i in range(s,t+1):
            capp+=1
    for i in resor:
        if i in range(s,t+1):
            cor+=1
    print(capp)
    print(cor)