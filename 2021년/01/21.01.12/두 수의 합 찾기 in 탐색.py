# in을 이용한 탐색

def twoSum(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))

# 타겟에서 첫 번째 값을 뺀 값이 존재하는지를 탐색하는 방법
# 전체 시간 복잡도는 brute force와 같은 O(n^2)
# 그러나 매번 값을 비교하는 것에 비해 내부함수 in을 이용하는 것이 더 빠르다