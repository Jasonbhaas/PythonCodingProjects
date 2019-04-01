
def threeSum(nums):
    nums.sort()
    results = []
    last = None
    cache = {}

    if len(nums) < 3:
        return results

    for i, val in enumerate(nums):
        if val != last:
            if last == 0

            last_val2 = None
            for val2 in nums[i + 1:]:
                if val2 != last_val2 and - 1 * (val + val2) in cache:
                    results.append([val, val2, -1 * (val + val2)])
                last_val2 = val2

            cache[val] = 1
        else:
            cache[val] += 1
            if cache[val] == 2 and val != 0:
                if -2 * val in cache:
                    results.append[val, val, -2 * val]

        last = val

    return results


threeSum[1, 2, -2, -1]
print(threeSum([-1, -1, -1, -1, -1, 2, 2, 2, -4]))
print(threeSum([0, 0]))

"""
    :type nums: List[int]
    :rtype: List[List[int]]






    cache = {}
    results = []

    nums.sort()
    last = None

    for i, val in enumerate(nums):
        if val != last:
            if val in cache:
                for tup in cache[val]:
                    val1 = tup[0]
                    val2 = tup[1]
                    results.append([[val, tup[0], tup[1]]])
                    if val1 in cache:
                        del cache[val1]
                    if val2 in cache:
                        del cache[val2]
                if val in cache:
                    del cache[val]

            for next_val in nums[i + 1:]:
                new_key = -1 * (val + next_val)
                if new_key in cache:
                    cache[new_key].append([val, next_val])
                else:
                    cache[new_key] = [[val, next_val]]

    return results
    """
