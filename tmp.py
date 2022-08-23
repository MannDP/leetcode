def soln(array, k):
    left = 0
    right = 0
    
    mx = float("-inf")
    sm = array[0]

    while(right < len(array)):
        if sm > k and left <= right:
            sm -= array[left]
            left += 1
        else:
            right += 1
            mx = max(mx, right-left)
            if right < len(array):
                sm += array[right]
            else:
                break
    
    return mx
        


print(soln([1,2,3], 4))
print(soln([3,1,2,1], 4))
print(soln([1,1,1,1,1,1], 6))
print(soln([9,1,1,1,1,1,1], 6))
print(soln([9,1,1,1,1,5,1,1], 6))
print(soln([9,1,1,1,1,2,1,1], 6))