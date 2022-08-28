def odd_strings(strings: list[str], m: int) -> str:
    res_even = True
    for s in strings:
        # determine parity of string
        s_even = True
        for c in s:
            c_even = True
            
            # raising to the power of m is useless
            # because even * even = even, and odd * odd = odd
            if ord(c) % 2 == 1:
                c_even = False
            
            # apply multiplication rule
            if s_even or c_even:
                s_even = True
            else:
                s_even = False

        # update parity of sum
        if (res_even and s_even) or (not res_even and not s_even):
            res_even = True
        else:
            res_even = False

    # print parity of the result down here
    return 'EVEN' if res_even else 'ODD'

print(odd_strings(['abc', 'abcd'], 2))

# multiplication rule:
# even * _ = even
# odd * odd = odd
# sum rule: odd + even = odd, odd + odd = even, even + even = even
# even + even = even
# odd + odd = even
# even + odd = odd
