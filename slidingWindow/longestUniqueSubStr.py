s = "prateekbhaiya"
i = 0
j = 0
m = {}
mwl = 0
sw = -1
wl = 0
while(j<len(s)):
    ch = s[j]
    if(ch in m and m[ch]>=i):
        i = m[ch] + 1
        wl = j - i
    
    m[ch] = j
    wl += 1
    j+=1
    if(wl>mwl):
        mwl = wl
        sw = i

print(s[sw:mwl+sw])
    
