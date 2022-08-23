def area(p1, p2, p3) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))


def dist(p1, p2) -> float:
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def points_belong(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, xp: int, yp: int, xq: int, yq: int) -> int:
    a = (x1, y1)
    b = (x2, y2)
    c = (x3, y3)
    ab = dist(a, b)
    ac = dist(a, c)
    bc = dist(b, c)

    # special case, non-degenerate
    if not (ab + bc > ac or bc + ac > ab or ab + ac > bc):
        return 0

    t_area = area(a, b, c)

    # check membership
    p = (xp, yp)
    p_area = area(p, a, b) + area(p, b, c) + area(p, a, c)
    q = (xq, yq)
    q_area = area(q, a, b) + area(q, b, c) + area(q, a, c)
    p_in = p_area == t_area
    q_in = q_area == t_area

    if p_in and q_in:
        return 3
    elif p_in:
        return 1
    elif q_in:
        return 2
    return 4


print(points_belong(2, 2, 7, 2, 5, 4, 4, 3, 7, 4) == 1)
print(points_belong(3, 1, 7, 1, 5, 5, 3, 1, 0, 0) == 1)
print(points_belong(3, 1, 7, 1, 5, 5, 1, 1, 4, 3) == 2)
print(points_belong(3, 1, 7, 1, 5, 5, 5, 2, 6, 3) == 3)
print(points_belong(3, 1, 7, 1, 5, 5, 1, 1, 2, 2) == 4)
