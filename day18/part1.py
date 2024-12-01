import pygame
import sys
from collections import deque

color: dict[tuple[int, int], str] = {}

instructions: list[tuple[str, int, str]] = []
with open("input.txt") as f:
    for line in f:
        data = line.split()
        (d, n, c) = (data[0], data[1], data[2])
        instructions.append((d, int(n), c[1:-1]))

curr = (0, 0)
for ins in instructions:
    d, n, c = ins
    if d == "U":
        update = (-1, 0)
    elif d == "R":
        update = (0, 1)
    elif d == "D":
        update = (1, 0)
    else:
        update = (0, -1)
    for _ in range(n):
        curr = (curr[0] + update[0], curr[1] + update[1])
        color[curr] = c

queue = deque([(1, 1)])
visited = set(color.keys())
while len(queue) > 0:
    coord = queue.popleft()
    i, j = coord
    color[coord] = "#09cdda"
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        new = (i + di, j + dj)
        if new not in visited:
            visited.add(new)
            queue.append(new)

print("Part 1: " + str(len(color)))

w = 2
draw_per_frame = 50
draw_every_frame = 1
color_list = list(color.items())
if len(sys.argv) > 1:
    _ = pygame.init()
    running = True
    screen = screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    dt = 0

    frame = 0
    curr_color = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if frame % draw_every_frame == 0 and curr_color < len(color_list):
            for _ in range(draw_per_frame):
                if curr_color >= len(color_list):
                    break
                (y, x), c = color_list[curr_color]
                _ = pygame.draw.rect(
                    screen, pygame.Color(c), pygame.Rect(x * w + 200, y * w + 300, w, w)
                )
                curr_color += 1
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        frame += 1
