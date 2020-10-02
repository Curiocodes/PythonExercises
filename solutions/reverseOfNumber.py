def reverse(n):
    temp = n
    r = 0
    while(temp!=0):
        last = temp % 10
        r=(r*10)+last
        temp = temp//10
    return r


rev = reverse(234)
print(rev)