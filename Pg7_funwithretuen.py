#with parameter with parameter
def calcuate(a,b,operation):
    #here it will check the operation string is present in the
    # list of the operators if present it will be evaluated
    if operation in ['+','-','*','/','%']:
        return eval(str(a) + operation + str(b))
    else:
        return "invalid operator"

print(calcuate(11,3,'/'))
