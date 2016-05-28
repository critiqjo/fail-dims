#!/bin/python2

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
  def __init__(self, xs, ys, zs, *args, **kwargs):
    FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
    self._verts3d = xs, ys, zs

  def draw(self, renderer):
    xs3d, ys3d, zs3d = self._verts3d
    xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
    self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
    FancyArrowPatch.draw(self, renderer)

def new_fig():
  fig = plt.figure()
  return fig.gca(projection='3d')

def save_fig(name):
  plt.savefig(name, bbox_inches="tight")

def set_ax_view(ax):
  ax.set_yticks(range(0, 100, 20))
  ax.set_xlim([0, 2000])
  ax.set_ylim([0, 80])
  ax.set_zlim([0, 1.2])
  ax.view_init(azim=-140)

def cdf(ax, x, y, z, end_x, end_y, z_start=0):
  xx = np.linspace(x, x, 2)
  yy = np.linspace(y, y, 2)
  zz = np.linspace(z_start, z, 2)
  ax.plot(xx, yy, zz, color="black")

  xx, yy = np.meshgrid(range(x, end_x, 25), range(y, end_y, 1))
  zz = 0 * xx + z
  ax.plot_surface(xx, yy, zz, color="cyan")

def pdf(ax, x, y, z):
  a = Arrow3D([x, x], [y, y], [0, z], mutation_scale=20, lw=1, arrowstyle="->", color="blue")
  ax.add_artist(a)

ax = new_fig()
pdf(ax, 500, 20, 1)
set_ax_view(ax)
save_fig("one-pdf.svg")

ax = new_fig()
cdf(ax, 500, 20, 1, 2000, 80)
set_ax_view(ax)
save_fig("one-cdf.svg")

ax = new_fig()
pdf(ax, 1000, 20, 0.5)
pdf(ax, 500, 40, 0.5)
set_ax_view(ax)
save_fig("two-pdf.svg")

ax = new_fig()
cdf(ax, 500, 40, 0.5, 1000, 80)
cdf(ax, 1000, 20, 0.5, 2000, 40)
cdf(ax, 1000, 40, 1, 2000, 80)
set_ax_view(ax)
save_fig("two-cdf.svg")

ax = new_fig()
pdf(ax, 500, 20, 0.25)
pdf(ax, 500, 40, 0.25)
pdf(ax, 1000, 40, 0.25)
pdf(ax, 1000, 20, 0.25)
set_ax_view(ax)
save_fig("twoi-pdf.svg")

ax = new_fig()
cdf(ax, 500, 20, 0.25, 1000, 40)
cdf(ax, 500, 40, 0.5, 1000, 80)
cdf(ax, 1000, 20, 0.5, 2000, 40)
cdf(ax, 1000, 40, 1, 2000, 80, z_start=0.25)
set_ax_view(ax)
save_fig("twoi-cdf.svg")
