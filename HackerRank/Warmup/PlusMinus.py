def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    count=0
    for i in arr:
        if(i>0):
            pos+=1
        if(i==0):
            zer+=1
        if(i<0):
            neg+=1
        count+=1
    print("%.6f"%(pos/count))
    print("%.6f"%(neg/count))
    print("%.6f"%(zer/count))