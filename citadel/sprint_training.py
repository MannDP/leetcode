def getmostvisited(n, sprints):
    arr = [0]*(n+2)
    for i in range(len(sprints)-1):
        start = min(sprints[i], sprints[i+1])
        end = max(sprints[i], sprints[i+1])
        arr[start] += 1
        arr[end + 1] -= 1
    ans = -1
    s = 0
    maxi = -1
    for i in range(1, n+1):
        arr[i] += s
        s = arr[i]
        if s > maxi:
            maxi = s
            ans = i

    return ans
