s=input()
l=["a","e","i","o","u","A","E","I","0","U"]
c=0
k=0
for i in s:
    if i in l:
        c+=1
    else:
        k+=1
print(c,k)
"""
o/p:
jahnavi
3 4
"""
