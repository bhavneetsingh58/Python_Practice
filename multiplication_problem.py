def adder(toMul,iter):
    sum=0
    for i in range(iter):
        sum=sum+toMul
        print(sum)
    return sum


def ValueDecider(iter,flag):
    iter1 = 0
    iter2 = 0
    iter1 = int(iter/2)
    iter2 = iter - iter1 
    if(flag == 0):return iter1
    else: return iter2

iter = 9
toMul = 5

sum1 = adder(toMul,ValueDecider(iter,0))
sum2 = adder(toMul,ValueDecider(iter,1))

print(sum1+sum2)
