from typing import List

# O(n) time, O(n) space
def stock_pairs(stocks_profit: List[int], target: int) -> int:
    used = set()
    set_stocks_profit = set(stocks_profit)
    res = 0

    for sp in stocks_profit:
        diff = target - sp
        if diff in set_stocks_profit:
            pair = [sp, diff]
            pair.sort()
            pair = tuple(pair)
            if pair not in used:
                used.add(pair)
                res += 1
    return res
