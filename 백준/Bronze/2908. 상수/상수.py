nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i][::-1])
print(max(nums))