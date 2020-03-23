import os, re
import numpy
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

past_infection_files = ["../../data/" + f for f in os.listdir("../../data") if f.startswith("memes_infections") and f.endswith(".log")]

print(past_infection_files)
