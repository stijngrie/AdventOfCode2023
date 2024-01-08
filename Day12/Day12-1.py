Lines = open('Day12/Day12-Input.txt', 'r').readlines()

def check(blocks, nums):
    if blocks == "":
        return 1 if nums == () else 0
    if nums == ():
        return 0 if "#" in blocks else 1
    
    amount = 0

    if blocks[0] in ".?":
        amount += check(blocks[1:], nums)

    if blocks[0] in "#?":
        if nums[0] <= len(blocks) and "." not in blocks[:nums[0]] and (nums[0] == len(blocks) or blocks[nums[0]] != "#"):
            amount += check(blocks[nums[0] + 1:], nums[1:])

    return amount

answer = 0
for line in Lines:
    blocks, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    answer += check(blocks, nums)

print(answer)