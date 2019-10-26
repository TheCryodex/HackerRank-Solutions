def getTotalX(a, b):
    # Write your code here
    count=0
    for i in range(a[len(a)-1], b[0]+1):
        x = True
        for j in range(len(a)):
            if(i%a[j]!=0):
                x = False
                break
            else:
                continue
        y = True

        for j in range(len(b)):
            if(b[j]%i!=0):
                y = False
                break
            else:
                continue
        
        if(x and y):
            count+=1
    return(count)