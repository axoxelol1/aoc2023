from PIL import Image
from itertools import product


n = 3

img = Image.new("RGB", (131 * n, 131 * n), (0, 0, 0))
with open("input.txt", "r") as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line):
            for sx, sy in product([131 * (i) for i in range(n)], repeat=2):
                if (x == 65 or y == 65) and char == ".":
                    img.putpixel((x + sx, y + sy), (255, 0, 0))
                elif (x in [0, 130] or y in [0, 130]) and char == ".":
                    img.putpixel((x + sx, y + sy), (0, 255, 0))
                elif char == "S":
                    img.putpixel((x + sx, y + sy), (0, 255, 0))
                elif char == ".":
                    img.putpixel((x + sx, y + sy), (0, 0, 0))
                if char == "#":
                    img.putpixel((x + sx, y + sy), (255, 255, 255))


img.save(f"{n}-input.png")
