from phi.flow import *
import math
v = StaggeredGrid(
    #1, 1, 1,
    values = lambda pos: vec(
        x = math.cos(pos).vector["X"] * math.sin(pos).vector["Y"],
        y = math.sin(pos).vector["X"] * math.cos(pos).vector["Y"],
    ),
    extrapolation=extrapolation.PERIODIC,
    x=25,
    y=25,
    bounds= Box(_x= 2 *PI, _y= 2 *PI),
)

import matplotlib.pyplot as plt
import numpy as np
plt.style.use("dark_background")

plot(v)