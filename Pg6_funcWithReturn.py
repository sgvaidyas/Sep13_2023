#with parameter without
def calcuate(a,b,operation):
    match operation:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return a/b
        case '%':
            return a%b
        case _:
            return "invalid choice"

print(calcuate(11,3,'+'))
res = calcuate(12,66,'-')
print(res)
print(calcuate(88,44,'&'))
newval = res*10
print(newval)