class Node:
    def __init__(self, id):
        self.id = id
        self.friends = set()

def get_group_size(people, student, other_student):
    # find size of connected component of student
    # if other_student is in the connected component, return True in tuple
    seen = False
    visited = set()
    queue = [student]
    while queue:
        node = queue.pop()
        if node in visited:
            continue
        visited.add(node)
        if other_student in people[node].friends:
            seen = True
        queue.extend(people[node].friends)
    return (len(visited), seen)

def getTheGroups(n, queryType, students1, students2):
    people = { i: Node(i) for i in range(1, n + 1) }

    totals = []
    for i, type in enumerate(queryType):
        if type == 'Friend':
            # make students friends
            people[students1[i]].friends.add(students2[i])
            people[students2[i]].friends.add(students1[i])
        elif type == 'Total':
            # find size of connected component of each student and add to totals
            size1, seen1 = get_group_size(people, students1[i], students2[i])
            size2, seen2 = get_group_size(people, students2[i], students1[i])
            if seen1 and seen2:
                totals.append(size1)
            else:
                totals.append(size1 + size2)

    return totals



def getTheGroups(n, queryType, students1, students2):
    res = []
    # each group is of size 1
    counts = [1 for _ in range(n + 1)]
    # parent of each node is itself
    parents = [i for i in range(n + 1)]

    def find_group(k: int) -> int:
        # find parent of node
        while True:
            if parents[k] == k:
                return k
            k = parents[k]

    # union find algorithm
    for i, q in enumerate(queryType):
        s1 = students1[i]
        s2 = students2[i]
        gs1 = find_group(s1)
        gs2 = find_group(s2)

        if q == 'Total':
            total = counts[gs1]
            if gs1 != gs2:
                total += counts[gs2]
            res.append(total)
            continue

        if gs1 == gs2:
            # same group, nothing to update
            continue
        # merge gs2 into gs1
        parents[gs2] = gs1
        counts[gs1] += counts[gs2]
        counts[gs2] = 0
    return res
