def diagonalDifference(arr):
    n=len(arr)
    sumld=0
    sumrd=0

    for i in range(0,n):
        sumld=sumld+arr[i][i]
    for i in range(0,n):
        sumrd=sumrd+arr[i][n-1]
        n-=1
    return(abs(sumld-sumrd))