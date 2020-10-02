def sumOfreverse(n):
    temp = n
    r = 0
    sum =0
    while(temp!=0):
        last = temp % 10
        sum += last
        r=(r*10)+last
        temp = temp//10
    return sum


sum = sumOfreverse(111)
print(sum)