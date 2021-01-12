def twoSum(nums, target):
    nums_map = {}
    # 키와 값을 바꾸어 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target-num]

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))

# nums 가 딕셔너리로 바뀌어 저장됨
# nums_map = { 2: 0, 7: 1, 11: 2, 15: 3}
# 이 때 target에서 첫 번째 수를 뺀 결과를 key로 찾는다
# 해당 key의 value가 첫 번째 수와 target을 만드는 수가 된다