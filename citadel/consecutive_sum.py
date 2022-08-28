# Python program to count number of ways to
# express N as sum of consecutive numbers.
 
def countConsecutive(N):
     
    # constraint on values of L gives us the
    # time Complexity as O(N ^ 0.5)
    count = 0
    L = 1
    while( L * (L + 1) < 2 * N):
        a = (1.0 * N - (L * (L + 1) ) / 2) / (L + 1)
        if (a - int(a) == 0.0):
            count += 1
        L += 1
    return count
 
# Driver code
 
N = 15
print (countConsecutive(N))
N = 10
print (countConsecutive(N))
 
# This code is contributed by Sachin Bisht
