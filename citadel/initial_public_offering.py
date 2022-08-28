from typing import List


# with a PQ, runtime is: O(n)
def get_unallotted_users(bids: List[List[int]], total_shares: int) -> List[int]:
    res = {uid for (uid, _, _, _) in bids}

    from collections import deque
    bids = deque(sorted(bids, key=lambda bid: (-bid[2], bid[3])))

    unallocated = total_shares
    while bids and unallocated > 0:
        # 0 = uid, 1 = num_shares, 2 = price
        group = [bids.popleft()]
        while bids and group[0][2] == bids[0][2]:
            group.append(bids.popleft())

        # allocate shares
        if len(group) == 1:
            bid = group[0]
            res.remove(bid[0])
            unallocated -= bid[1]
            continue

        # distribute shares in group
        if len(group) <= unallocated:
            for bid in group:
                res.remove(bid[0])
                unallocated -= bid[1]
        else:
            i = 0
            while unallocated > 0:
                bid = group[i]
                res.remove(bid[0])
                unallocated -= 1
                i += 1
    return list(res)


print(get_unallotted_users([[1, 5, 5, 0], [2, 7, 8, 1], [3, 7, 5, 1], [4, 10, 3, 3]], 18) == [4])
print(get_unallotted_users([[1, 2, 5, 0], [2, 1, 4, 2], [3, 5, 4, 6]], 3) == [3])
print(get_unallotted_users([[1, 2, 3, 5]], 3) == [])
print(get_unallotted_users([[1, 1, 10, 1], [2, 3, 5, 2], [3, 4, 5, 3], [4, 1, 5, 4], [5, 10, 1, 5]], 9) == [5])
