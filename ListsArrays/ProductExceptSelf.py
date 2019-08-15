import copy


def productExceptSelf(nums):
    length = len(nums)
    result = copy.deepcopy(nums)
    previous_left = nums[0]
    previous_right = result[-1]
    nums[0] = 1
    result[-1] = 1

    for i in range(1, length):
        nums[i], previous_left = nums[i - 1] * previous_left, nums[i]
        result[length - i - 1], previous_right = result[length - i] * \
            previous_right, result[length-i - 1]

    for i in range(length):
        result[i] *= nums[i]

    return result


print(productExceptSelf([1, 2, 3, 4]))
