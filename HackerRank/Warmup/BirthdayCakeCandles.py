def birthdayCakeCandles(ar):
    maxelement=ar[0]
    count=0
    for i in ar:
        if i > maxelement:
            maxelement=i
    for i in ar:
        if i==maxelement:
            count+=1
    return(count)