a =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for k,v in freq.items():
    print(k,v)





""""
1 5
5 2
3 3
4 3
2 4"""
