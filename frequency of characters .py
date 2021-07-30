s = input()
f = {}
for i in s:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1
print (str(f))
"""
o/p:
jaannnu
{'n': 3, 'u': 1, 'j': 1, 'a': 2}
"""
