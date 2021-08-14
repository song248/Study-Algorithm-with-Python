nums = input()
answer = int(nums[0])
for i in range(1, len(nums)):
    if int(nums[i]) == 1 or answer == 0:
        answer += int(nums[i])
    else:
        answer *= int(nums[i])
print(answer)