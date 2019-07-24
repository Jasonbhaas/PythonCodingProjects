def maxPoints(elements):

    if len(elements) == 0:
        return 0
    elements.sort(reverse=True)

    largest_num = elements[0]

    helper_cache = [0] * (largest_num + 4)

    prev_num = 0
    sum_so_far = 0
    max_so_far = 0
    for num in elements:
        if prev_num != num:
            sum_so_far = 0
        sum_so_far += num
        # to ensure that if/when there's a gap in sequential numbers,
        # that the points carry through
        if prev_num - num > 2 and helper_cache[num + 2] == 0:
            helper_cache[num + 2] = max_so_far

        helper_cache[num] = sum_so_far + \
            max(helper_cache[num + 2], helper_cache[num + 3])

        max_so_far = max(helper_cache[num], max_so_far)
        prev_num = num

    return max_so_far


elements = [1, 2, 1, 3, 2, 3, 8]

print(maxPoints(elements))
