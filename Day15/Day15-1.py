text = open('Day15/Day15-Input.txt', 'r').read().splitlines()[0]
def hash(text):
    value = 0
    for char in text:
        value += ord(char)
        value *= 17
        value %= 256
    return value
print(sum(map(hash, text.split(","))))