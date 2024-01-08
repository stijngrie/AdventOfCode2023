file = open('Day13/Day13-Input.txt', 'r')

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above,below)) == 1:
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