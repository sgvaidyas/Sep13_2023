#function with parameters and without return
def welcomemsg(name,sub):
    print("Welcome to ",sub.upper()," bootcamp : ",name.upper())

master = [["shilpa","python"], ["Praksh","Java"],["Siva","CPP"]]
for x in master:
    welcomemsg(x[0],x[1])



'''#call fun
welcomemsg("shilpa","python")
welcomemsg("Rahul","C++")
welcomemsg("Tejal","Java")'''

