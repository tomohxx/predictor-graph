# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html
# https://matplotlib.org/stable/api/font_manager_api.html?highlight=font#module-matplotlib.font_manager
# https://matplotlib.org/stable/api/matplotlib_configuration_api.html
import sys

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

from predictor import Predictor


if len(sys.argv) != 2:
    print("Error argument")
    sys.exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()
    m = int(lines[0])
    wall = []
    river = []

    for line in lines[1:]:
        left, furiten = line.split()[1:3]
        wall.append(int(left))
        river.append(int(furiten))

assert len(wall) == 34
assert len(river) == 34

predictor = Predictor()
predictor.initialize("/predictor/data")

total, *others = predictor(wall, river, m)
props = [[s / total.all for s in o.states] for o in others]

font_manager.fontManager.addfont("/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf")
matplotlib.rc("font", family="IPAGothic")

labels = [
    "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",
    "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
    "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",
    "東", "南", "西", "北", "白", "発", "中"]
width = 0.5

fig, ax = plt.subplots()

ax.bar(labels, props[0], width, label="一般形")
ax.bar(labels, props[1], width, label="七対子", bottom=props[0])
ax.bar(labels, props[2], width, label="国士無双", bottom=props[1])

ax.set_xlabel("待ち")
ax.set_ylabel("割合")
ax.set_title("全ての聴牌形に対する待ち毎の聴牌形の割合")
ax.grid(True, "major", "y", ls="--")
ax.tick_params("x", labelrotation=90)
ax.legend(fontsize="x-small")

fig.savefig("/output/img.png")
