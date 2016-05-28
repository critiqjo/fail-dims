#!/bin/python2

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

def new_fig(xlim):
  fig = plt.figure()
  ax = fig.gca()
  ax.set_xlim([0, xlim])
  ax.set_ylim([0, 1.04])
  return ax

def save_fig(name):
  plt.savefig(name, bbox_inches="tight")

def pdf(ax, xs):
  ht = 1. / len(xs)
  for x in xs:
    ax.annotate("", xy=(x, ht), xytext=(x, 0),
      arrowprops=dict(arrowstyle="->"))

def cdf(ax, xs):
  ht = 1.0 / len(xs)
  xs = [0] + xs
  ys = [ht * i for i in range(0, len(xs))]
  ax.step(xs + [ax.get_xlim()[1]], ys + [1], where="post")

ax = new_fig(2000)
pdf(ax, [500])
save_fig("onex-pdf.svg")

ax = new_fig(80)
pdf(ax, [20])
save_fig("oney-pdf.svg")

ax = new_fig(2000)
cdf(ax, [500])
save_fig("onex-cdf.svg")

ax = new_fig(80)
cdf(ax, [20])
save_fig("oney-cdf.svg")

ax = new_fig(2000)
pdf(ax, [500, 1000])
save_fig("twox-pdf.svg")

ax = new_fig(80)
pdf(ax, [20, 40])
save_fig("twoy-pdf.svg")

ax = new_fig(2000)
cdf(ax, [500, 1000])
save_fig("twox-cdf.svg")

ax = new_fig(80)
cdf(ax, [20, 40])
save_fig("twoy-cdf.svg")
