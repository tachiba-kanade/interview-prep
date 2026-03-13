# class Camera:

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.distance = 5

#     def project(self, vector):

#         x, y, z = vector.data

#         # prevent division by zero
#         if z + self.distance == 0:
#             z += 0.0001

#         factor = 400 / (z + self.distance)

#         screen_x = x * factor + self.width / 2
#         screen_y = -y * factor + self.height / 2

#         return (int(screen_x), int(screen_y))

import math


class Camera:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.distance = 15

        self.yaw = 0
        self.pitch = -0.4

        self.sensitivity = 0.005

    def rotate(self, dx, dy):

        self.yaw += dx * self.sensitivity
        self.pitch += dy * self.sensitivity

        # limit vertical rotation
        self.pitch = max(-1.5, min(1.5, self.pitch))

    def project(self, vector):

        x, y, z = vector.data

        # --- Y rotation (yaw) ---
        cos_y = math.cos(self.yaw)
        sin_y = math.sin(self.yaw)

        xz = x * cos_y - z * sin_y
        zz = x * sin_y + z * cos_y

        x = xz
        z = zz

        # --- X rotation (pitch) ---
        cos_p = math.cos(self.pitch)
        sin_p = math.sin(self.pitch)

        yz = y * cos_p - z * sin_p
        zz = y * sin_p + z * cos_p

        y = yz
        z = zz

        z += self.distance

        if z <= 0:
            return None

        factor = 400 / z

        screen_x = x * factor + self.width / 2
        screen_y = -y * factor + self.height / 2

        return (int(screen_x), int(screen_y))