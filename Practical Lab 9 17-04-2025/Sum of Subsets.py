def sum_of_subsets(nums, target):
    result = []

    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path[:])
            return
        if current_sum > target:
            return
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i])
            path.pop()

    backtrack(0, [], 0)
    return result

nums = [2, 4, 6, 8]
target = 8
print(sum_of_subsets(nums, target))
