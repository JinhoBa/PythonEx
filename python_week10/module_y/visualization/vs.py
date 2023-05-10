import matplotlib.pyplot as plt
from understat import Understat
import pandas as pd
import numpy as np
import seaborn as sns
import asyncio
import json
import aiohttp
from understat import Understat
import nest_asyncio
# to avoid errors apply the nest asyncio 
nest_asyncio.apply()

player_id = "647"
season = "2019"
player_name = "Lionel Messi"

understat = Understat()

data = understat.get_league_players_data("epl", 2020)
xG = []
xG90 = []
shots = []
key_passes = []
date = []
npg = []



for match in data:
    xG.append(float(match["xG"]))
    xG90.append(float(match["xG90"]))
    shots.append(int(match["shots"]))
    key_passes.append(int(match["key_passes"]))
    npg.append(int(match["npg"]))
    date.append(match["datetime"])

fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle(f"{player_name} ({season})")

axs[0, 0].plot(date, xG, "bo-", linewidth=2, markersize=10, alpha=0.7)
axs[0, 0].set_title("xG per game")

plt.show()