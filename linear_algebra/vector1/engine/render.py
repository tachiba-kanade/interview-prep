# import pygame
# from linalg.vector import Vector


# class Renderer:

#     def __init__(self, screen, camera):
#         self.screen = screen
#         self.camera = camera

#     def draw_vector(self, vector, color=(255,255,255)):

#         origin = self.camera.project(Vector([0,0,0]))
#         end = self.camera.project(vector)

#         pygame.draw.line(self.screen, color, origin, end, 3)
#         pygame.draw.circle(self.screen, color, end, 5)

#     def draw_grid(self, size=10, step=1):

#         grid_color = (50,50,50)

#         # lines parallel to Z axis
#         for x in range(-size, size+1, step):

#             start = Vector([x, 0, -size])
#             end   = Vector([x, 0,  size])

#             p1 = self.camera.project(start)
#             p2 = self.camera.project(end)

#             pygame.draw.line(self.screen, grid_color, p1, p2, 1)

#         # lines parallel to X axis
#         for z in range(-size, size+1, step):

#             start = Vector([-size, 0, z])
#             end   = Vector([ size, 0, z])

#             p1 = self.camera.project(start)
#             p2 = self.camera.project(end)

#             pygame.draw.line(self.screen, grid_color, p1, p2, 1)

import pygame
from linalg.vector import Vector


class Renderer:

    def __init__(self, screen, camera):

        self.screen = screen
        self.camera = camera

    def draw_vector(self, vector, color=(255,255,255)):

        origin = self.camera.project(Vector([0,0,0]))
        end = self.camera.project(vector)

        if origin and end:
            pygame.draw.line(self.screen, color, origin, end, 3)
            pygame.draw.circle(self.screen, color, end, 5)

    def draw_grid(self, size=50, step=1):

        grid_color = (50,50,50)

        # X lines
        for x in range(-size, size+1, step):

            start = Vector([x,0,-size])
            end   = Vector([x,0,size])

            p1 = self.camera.project(start)
            p2 = self.camera.project(end)

            if p1 and p2:
                pygame.draw.line(self.screen, grid_color, p1, p2, 1)

        # Z lines
        for z in range(-size, size+1, step):

            start = Vector([-size,0,z])
            end   = Vector([size,0,z])

            p1 = self.camera.project(start)
            p2 = self.camera.project(end)

            if p1 and p2:
                pygame.draw.line(self.screen, grid_color, p1, p2, 1)

    def draw_axes(self):

        axes = [
            (Vector([5,0,0]), (255,0,0)),   # X
            (Vector([0,5,0]), (0,255,0)),   # Y
            (Vector([0,0,5]), (0,0,255)),   # Z
        ]

        origin = self.camera.project(Vector([0,0,0]))

        for v, color in axes:

            end = self.camera.project(v)

            if origin and end:
                pygame.draw.line(self.screen, color, origin, end, 3)