#when a function returns more than 1 value
def evenodd(l):
    odd =[]
    even =[]
    for x in l:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    else:
        return even,odd

evennum,oddnum = evenodd([11,2,33,4,55,66,9])
print("EVEN NUM = ",evennum)
print("ODD NUM = ",oddnum)
res = evenodd([10,222,3333,9])
print("Even  = ",res[0], " Odd  = ",res[1])