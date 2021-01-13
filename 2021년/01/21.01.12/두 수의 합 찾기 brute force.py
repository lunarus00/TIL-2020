# 모든 조합에 대해 확인

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))

# 주어진 리스트와 결과에 대해 모든 조합을 확인
# 알맞은 결과가 있을경우 return