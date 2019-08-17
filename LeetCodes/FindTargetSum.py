def findTargetSum(numbers, target):
    results = []

    def dfs(nums, combination, path):
        if len(nums) == 0:
            if combination == 0:
                results.append(path[1:])
        else:
            for i in range(0, len(nums), 1):
                number = nums[:i+1]
                dfs(nums[i+1:], combination - int(number), path + "+" + number)
                dfs(nums[i+1:], combination + int(number), path + "-" + number)

    dfs(numbers, target, "")
    return results


print(findTargetSum("123456789", 100))
