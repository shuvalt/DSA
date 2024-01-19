arr = [1,3,2,1,4,1,3,2,1,1,2]
k = 8
i = 0
j = 0
cs = 0
sw = []
while(j<len(arr)):
    cs += arr[j]
    j+=1
    while(cs>k and i<j):
        cs -= arr[i]
        i+=1
    if(cs==k):
        print(i,j-1)
        sw.append(j-i)
        
print(min(sw))
    
