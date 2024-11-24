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

# Without tuple
def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, 0, {})

def _non_adjacent_sum(nums, i, memo):
  if i >= len(nums):
    return 0
  if i not in memo:
    include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
    exclude = _non_adjacent_sum(nums, i + 1, memo)
    memo[i] = max(include, exclude)
  return memo[i]