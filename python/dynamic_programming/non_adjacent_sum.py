# https://www.structy.net/problems/non-adjacent-sum

def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums, {})


def _non_adjacent_sum(nums, memo):
    if len(nums) == 1:
        return nums[0]
    if not nums:
        return 0

    key = tuple(nums)
    if key not in memo:
        with_first = _non_adjacent_sum(nums[1:], memo)
        without_first = _non_adjacent_sum(nums[2:], memo) + nums[0]
        memo[key] = max(with_first, without_first)

    return memo[key]