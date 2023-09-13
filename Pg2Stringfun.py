'''
a = "this is a sample text"
print(a.capitalize())
print(a.title())
print(a.upper())
a = "UIUIUIssdd"
print(a.lower())
'''
'''
a = " apple mango grapes"
print(a.count("pp"))
a="star"
print(a.center(90),"****")
print(a.center(90,"*"))
print(a.ljust(90,"*"))
print(a.rjust(90,"*"))

#print(a.center(90,"*"))
'''
'''
a = "apple"
print(a.islower())
a="klklJHH"
print(a.islower())
a = "APPLE"
print(a.isupper())
'''
'''
a ="   Shilpa         Vaidya        "
print(a.strip())
print(a.lstrip())
print(a.rstrip())
'''
a = " hi   this   is a sentence with uneven   space"
x = a.split()
print(x)
print(" ".join(a.split()))
a = " hi   this   is, a sentence with, uneven   space"
x = a.split(',')
print(x)
a = "agjhUIUHJK"
print(a.swapcase())
