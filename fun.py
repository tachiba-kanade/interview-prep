import pygame
import math

pygame.init()

# Fullscreen display
s = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

w = s.get_width()
h = s.get_height()
clock = pygame.time.Clock()

# Points: [x, y, old_x, old_y, pinned]
P = [
    [x * 20 + w / 4, y * 20 + 100, x * 20 + 100, y * 20 + 100, y == 0]
    for y in range(30)
    for x in range(50)
]

# Sticks: [point1_index, point2_index, active]
S = (
    [[i, i + 1, 1] for i in range(len(P)) if (i + 1) % 50] +
    [[i, i + 50, 1] for i in range(len(P) - 50)]
)

running = True
while running:

    # Exit on ESC
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    s.fill((0, 5, 10))

    mx, my = pygame.mouse.get_pos()
    md = pygame.mouse.get_pressed()

    # Update points (Verlet integration)
    for p in P:
        if not p[4]:  # not pinned

            if md[0] and math.hypot(p[0] - mx, p[1] - my) < 30:
                p[0], p[1] = mx, my

            vx = max(-20, min(20, (p[0] - p[2]) * 0.99))
            vy = max(-20, min(20, (p[1] - p[3]) * 0.99))

            p[2], p[3] = p[0], p[1]
            p[0] += vx
            p[1] += vy + 0.4  # gravity

    # Constraint solving
    for _ in range(6):
        for sk in [k for k in S if k[2]]:
            p1 = P[sk[0]]
            p2 = P[sk[1]]

            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            d = math.hypot(dx, dy) or 0.1

            # Break stick
            if d > 100 or (
                md[2] and
                math.hypot((p1[0] + p2[0]) / 2 - mx,
                           (p1[1] + p2[1]) / 2 - my) < 15
            ):
                sk[2] = 0
                continue

            f = (20 - d) / d * 0.5

            if not p1[4]:
                p1[0] -= dx * f
                p1[1] -= dy * f

            if not p2[4]:
                p2[0] += dx * f
                p2[1] += dy * f

    # Draw sticks
    for p1, p2, active in [k for k in S if k[2]]:
        pygame.draw.line(
            s,
            (0, 255, 150),
            (P[p1][0], P[p1][1]),
            (P[p2][0], P[p2][1]),
            2
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()