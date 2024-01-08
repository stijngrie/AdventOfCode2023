file = open('Day13/Day13-Input.txt', 'r')

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        above = above[:len(below)]
        below = below[:len(above)]

        if above == below:
            return r
    return 0
        
answer = 0
for block in file.read().split("\n\n"):
    grid = block.splitlines()
    row = find_mirror(grid)
    answer += row * 100
    col = find_mirror(list(zip(*grid)))
    answer += col

print(answer)  