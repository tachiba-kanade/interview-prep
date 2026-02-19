import pygame
import math

pygame.init()

# Fullscreen window
s = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W, H = s.get_size()
clock = pygame.time.Clock()

# Points: [x, y, old_x, old_y, pinned]
P = [
    [x * 20 + 200, y * 20 + 50,
     x * 20 + 200, y * 20 + 50,
     y == 0]
    for y in range(35)
    for x in range(55)
]

# Sticks: [index1, index2, active]
S = (
    [[i, i + 1, 1] for i in range(len(P)) if (i + 1) % 55] +
    [[i, i + 55, 1] for i in range(len(P) - 55)]
)

while True:

    # Exit handling
    for e in pygame.event.get():
        if (
            e.type == pygame.QUIT or
            (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE)
        ):
            pygame.quit()
            exit()

    s.fill((5, 5, 15))

    mx, my = pygame.mouse.get_pos()
    md = pygame.mouse.get_pressed()

    # Update points (Verlet integration)
    for p in P:
        if not p[4]:  # not pinned

            # Drag with left mouse
            if md[0] and math.hypot(p[0] - mx, p[1] - my) < 35:
                p[0], p[1] = mx, my

            # Verlet motion
            new_x = p[0] + (p[0] - p[2]) * 0.98
            new_y = p[1] + (p[1] - p[3]) * 0.98 + 0.5  # gravity

            p[2], p[3] = p[0], p[1]
            p[0], p[1] = new_x, new_y

    # Constraint solving
    for _ in range(5):
        for sk in [k for k in S if k[2]]:

            p1 = P[sk[0]]
            p2 = P[sk[1]]

            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            d = math.hypot(dx, dy)

            # Break stick
            if (
                d > 70 or
                (md[2] and
                 math.hypot((p1[0] + p2[0]) / 2 - mx,
                            (p1[1] + p2[1]) / 2 - my) < 20)
            ):
                sk[2] = 0
                continue

            f = (20 - d) / (d or 0.1) * 0.5

            if not p1[4]:
                p1[0] -= dx * f
                p1[1] -= dy * f

            if not p2[4]:
                p2[0] += dx * f
                p2[1] += dy * f

    # Draw sticks
    for p1, p2, active in [k for k in S if k[2]]:
        c = pygame.Color(0)
        c.hsva = (
            (P[p1][0] * 0.1 + pygame.time.get_ticks() * 0.1) % 360,
            100,
            100,
            100
        )

        pygame.draw.line(
            s,
            c,
            (P[p1][0], P[p1][1]),
            (P[p2][0], P[p2][1]),
            2
        )

    pygame.display.flip()
    clock.tick(60)