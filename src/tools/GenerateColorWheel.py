'''
Created on May 20, 2016

@author: Daniel Labbe
'''

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import cos, sin
from matplotlib.colors import ListedColormap
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color


def draw_lab_circle():

    L = 70
    r = 60

    lab_colors = []
    rgb_colors = []
    angle = 0

    #lab = LabColor(70,20,38)

    while (angle < 2 * np.pi):
        a = 20 + r * cos(angle)
        b = 38 + r * sin(angle)
        lab = LabColor(L, a, b)
        lab_colors.append(lab)
        angle += (2 * np.pi)/180

    for lab_color in lab_colors:
        srgb = convert_color(lab_color, sRGBColor)
        color = (srgb.clamped_rgb_r,  srgb.clamped_rgb_g, srgb.clamped_rgb_b)
        #color = srgb.get_value_tuple()
        print color
        rgb_colors.append(color)

    return rgb_colors

colors = draw_lab_circle()

lcm = ListedColormap(colors)

fig = plt.figure()

display_axes = fig.add_axes([0.1,0.1,0.8,0.8], projection='polar')
display_axes._direction = 2*np.pi

norm = mpl.colors.Normalize(0.0, 2*np.pi)

quant_steps = 2056#180
cb = mpl.colorbar.ColorbarBase(display_axes, cmap=lcm,#cmap=cm.get_cmap('hsv',quant_steps),
                                   norm=norm,
                                   orientation='horizontal')

cb.outline.set_visible(False)
display_axes.set_rlim([-1,1])
display_axes.set_axis_off()
plt.show() # Replace with plt.savefig if you want to save a file

