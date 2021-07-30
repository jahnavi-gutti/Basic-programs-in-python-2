s=input() 
for i in range(0, len(s)):  
    c = 1;  
    for j in range(i+1, len(s)):  
        if(s[i] == s[j] and s[i] != ' '):  
            c = c + 1;  
            s = s[:j] + '0' + s[j+1:]; 
              
    if(c > 1 and s[i] != '0'):  
        print(s[i])
"""
o/p
Jahnavi
a
"""
