def numberGame(nums):
    arr = []
    nums = sorted(nums)
    while len(nums) != 0:
        alice = nums.pop(0)
        bob = nums.pop(0)
        arr.append(bob)
        arr.append(alice)
    return arr

print(numberGame([5, 4, 2, 3]))