def hackerCards(collection, d):
    # greedy algorithm
    res = []
    collection = set(collection)

    for i in range(1, d + 1):
        if i > d:
            break
        if i in collection:
            continue
        res.append(i)
        d -= i
    return res


print(hackerCards([2, 4, 5], 7) == [1, 3])
# https://leetcode.com/discuss/interview-question/1536950/Twitter-OA-or-2022-Twitter-Early-Career-Engineering-Coding-Challenge-(Questions-and-Solutions)
