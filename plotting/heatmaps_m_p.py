import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_heatmap(df, value_col, title, outpath=None):
    # pivot to m x p grid
    pivot = df.pivot(index="m", columns="p", values=value_col).sort_index().sort_index(axis=1)

    fig, ax = plt.subplots(figsize=(7, 5))
    im = ax.imshow(pivot.values, aspect="auto", origin="lower")

    # ticks and labels
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns)
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)

    ax.set_xlabel("p")
    ax.set_ylabel("m")
    ax.set_title(title)

    # annotate each cell
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            val = pivot.iloc[i, j]
            if pd.notna(val):
                ax.text(j, i, f"{val:.3g}", ha="center", va="center", fontsize=12)

    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label(value_col)

    fig.tight_layout()

    if outpath is not None:
        fig.savefig(outpath, dpi=300, bbox_inches="tight")

    plt.show()


# ------------------------------------------------------------------------------
# load  csv
# -----------------------------
csv_path = "lc_qaoa_aqc_table.csv"   # change this
df = pd.read_csv(csv_path)

# output folder
outdir = Path("heatmaps_lc")
outdir.mkdir(exist_ok=True)



# clean column names if needed
df.columns = [c.strip() for c in df.columns]

# if CSV has names like "2Q Depth", "Feasible Samples", etc., it will work directly
# otherwise rename columns here:
# df = df.rename(columns={
#     "2Q Depth": "2Q Depth",
#     "Iterations": "Iterations",
#     "Feasible Samples": "Feasible Samples",
#     "Unique Feasible Bitstrings": "Unique Feasible Bitstrings",
# })

# make sure m and p are numeric
df["m"] = pd.to_numeric(df["m"])
df["p"] = pd.to_numeric(df["p"])



# -----------------------------
# make heatmaps
# -----------------------------
#plot_heatmap(
#    df,
#    value_col="2Q Depth",
#    title="2Q Depth on (m, p) Grid",
#    outpath=outdir / "heatmap_2q_depth.png",
#)

#plot_heatmap(
#    df,
#    value_col="Iterations",
#    title="Iterations on (m, p) Grid",
#    outpath=outdir / "heatmap_iterations.png",
#)

#plot_heatmap(
#    df,
#    value_col="Feasible Samples",
#    title="Feasible Samples on (m, p) Grid",
#    outpath=outdir / "heatmap_feasible_samples.png",
#)

#plot_heatmap(
#    df,
#    value_col="Unique Feasible Bitstrings",
#    title="Unique Feasible Bitstrings on (m, p) Grid",
#    outpath=outdir / "heatmap_unique_feasible_bitstrings.png",
#)

plot_heatmap(
    df,
    value_col="final_objective",
    title="Final Average QUBO Objective Value" ,
    outpath=outdir / "heatmap_objective.png",
)
