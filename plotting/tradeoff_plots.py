import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.rcParams['font.size'] = 16

from matplotlib.colors import LinearSegmentedColormap

cmap_custom = LinearSegmentedColormap.from_list(
    "rygb",
    ["red", "yellow", "green", "blue"]
)


df_plot = pd.read_csv('TSP_rensselaer_5n_aqc_alpha_fixedranks.csv')    

# remove rows where best feasible rank is missing
df_plot = df_plot.dropna(subset=['best_feasible_bitstring_rank_by_count'])

# scale marker sizes nicely
sizes = 100 + 600 * (
    (df_plot['feasible_counts'] - df_plot['feasible_counts'].min()) /
    (df_plot['feasible_counts'].max() - df_plot['feasible_counts'].min() + 1e-9)
)

plt.figure(figsize=(10, 8))

sc = plt.scatter(
    df_plot['full_two_qubit_depth'],
    df_plot['num_feasible_bitstrings'],
    s=sizes,
    c=df_plot['alpha'],
    cmap=cmap_custom,
    alpha=1
)

# annotate rank of best solution
for _, row in df_plot.iterrows():
    plt.text(
        row['full_two_qubit_depth'],
        row['num_feasible_bitstrings'],
        f"{int(row['best_feasible_bitstring_rank_by_count'])}",
        fontsize=12
    )

plt.xlabel('Full two-qubit depth')
plt.ylabel('Number of feasible solutions')
plt.title('Depth–Feasibility–Compression Tradeoff')

cbar = plt.colorbar(sc)
cbar.set_label('Compressed layers (alpha)')

plt.grid()
plt.show()


sizes = 100 + 600 * (
    (df_plot['feasible_counts'] - df_plot['feasible_counts'].min()) /
    (df_plot['feasible_counts'].max() - df_plot['feasible_counts'].min() + 1e-9)
)

plt.figure(figsize=(10, 8))

sc = plt.scatter(
    df_plot['alpha'],
    df_plot['best_feasible_bitstring_rank_by_count'],
    s=sizes,
    c=df_plot['full_two_qubit_depth'],
    cmap=cmap_custom,
    alpha=1
)

#for _, row in df_plot.iterrows():
#    plt.text(
#        row['alpha'],
#        row['best_feasible_bitstring_rank_by_count'],
#        f"{int(row['num_feasible_bitstrings'])}",
#        fontsize=12
#    )

plt.xlabel('$m$')
plt.ylabel('Rank of best solution (lower is better)')
plt.title('Effect of Compression on Best-Solution Concentration')

cbar = plt.colorbar(sc)
cbar.set_label('Two-qubit depth')

plt.grid()
plt.show()
