from collections import OrderedDict
def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))
str = "geeksforgeeks"
print ("With Order = ",removeDupWithOrder(str))
"""
o/p:
With Order =  geksfor
"""
