def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    count = 0

    if k < 0:
        return count

    product_so_far = 1
    left = 0

    for right in range(len(nums)):
        product_so_far *= nums[right]
        while product_so_far >= k and left < len(nums):
            product_so_far /= nums[left]
            left += 1

        if left <= right:
            count += right - left + 1

    return count
