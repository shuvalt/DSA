def trap_rain(height):
    traped_water = 0
    left = []
    right = []
    current_height = height[0]
    for i in range(len(height)):
        if(height[i]>current_height):
            current_height = height[i]
            left.append(height[i])
        else:
            left.append(current_height)
    current_r_height = height[len(height)-1]
    for i in range(len(height)-1,-1,-1):
        if(height[i]>current_r_height):
            current_r_height = height[i]
            right.insert(0,height[i])
        else:
            right.insert(0,current_r_height)
    for i in range(len(height)):
        t = min(left[i],right[i])
        traped_water += (t-height[i])
    return traped_water
    

print(trap_rain([0,1,0,2,1,0,1,3,2,1,2,1]))
