def f17():
    with open('17.txt') as f:
        a=[int(x) for x in f]
    mn=min(x for x in a if x % 17==0)
    maxi = -10
    count = 0
    for i in range(len(a)-1):
        if a[i]%mn ==0 or a[i+1]%mn == 0:
            sum = a[i+1]+a[i]
            count +=1
            if maxi < sum:
                maxi = sum
    print(maxi,count)
f17()
