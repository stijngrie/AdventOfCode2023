text = open('Day15/Day15-Input.txt', 'r').read().splitlines()[0]
def hash(text):
    value = 0
    for char in text:
        value += ord(char)
        value *= 17
        value %= 256
    return value

boxes = [[] for _ in range(256)]
focal_lengths = {}

for instruction in text.split(","):
    if "-" in instruction:
        label = instruction[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)
    else:
        label, length = instruction.split("=")
        length = int(length)

        index = hash(label)
        if label not in boxes[index]:
            boxes[index].append(label)
        focal_lengths[label] = length

answer = 0

for box_number, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box, 1):
        answer += box_number * lens_slot * focal_lengths[label]

print(answer)