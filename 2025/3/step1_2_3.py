import sys


def part1(nums):
    return sum(set(nums))


def part2(nums):
    nums = sorted(list(set(nums)))
    return sum(nums[:20])


def part3(nums):
    i = 0
    while nums:
        i += 1
        uniq = set(nums)
        for u in uniq:
            nums.remove(u)
    return i


nums = list(map(int, sys.stdin.readline().split(",")))


print("Step 1:", part1(nums))
print("Step 2:", part2(nums))
print("Step 3:", part3(nums))
