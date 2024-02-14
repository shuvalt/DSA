arr = [16,17,4,3,5,2]
current_max = arr[len(arr)-1]
n = len(arr)-1
for i in range(n,-1,-1):
    current = arr[i]
    if(i == n):
        arr[i] = -1
    else:
        arr[i] = current_max
    if(current>current_max):
        current_max = current
        
print(arr)
