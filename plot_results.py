import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

with open("results.json", "r") as f:
    results = json.load(f)

with open("degree_distributions.json", "r") as f:
    degree_distributions = json.load(f)

n_values = [2**i for i in range(7, 19)]

colors = {
    "barabasi": "#1f4e79",
    "erdos": "#ff8c00"
}

names = {
    "barabasi": "Barabasi-Albert",
    "erdos": "Erdos-Renyi"
}

# =========================
# DIAMETER PLOTS
# =========================

for model in ["barabasi", "erdos"]:

    plt.figure(figsize=(10,6))

    y = results[model]["diameter"]
    log_reference = np.log2(n_values)

    plt.plot(
        n_values,
        log_reference,
        color="green",
        linestyle=":",
         linewidth=2,
         label="Scaled log₂(n)"
    )

    plt.plot(
        n_values,
        y,
        marker="o",
        linewidth=2.5,
        color=colors[model],
        label = "Measure Diameter"
    )

    x_log = np.log2(n_values)

    slope, intercept = np.polyfit(
        x_log,
        y,
        1
    )

    fit_y = slope * x_log + intercept

    plt.plot(
        n_values,
        fit_y,
        color="#d62728",
        linestyle="--",
        linewidth=2,
        label=f"Fit (slope={slope:.3f})"
    )

    plt.xscale("log", base=2)
    ax = plt.gca()
    ax.yaxis.set_major_locator(MultipleLocator(1))

    plt.xticks(
        n_values,
        [f"2^{i}" for i in range(7,19)],
        rotation=45
    )

    plt.grid(
        True,
        linestyle="--",
        alpha=0.4
    )

    plt.xlabel("Number of Vertices (n)")
    plt.ylabel("Average Diameter")

    plt.title(
        f"{names[model]} Diameter vs Number of Vertices"
    )
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        f"{model}_diameter_plot.png",
        dpi=300
    )

    plt.close()


# =========================
# CLUSTERING PLOTS
# =========================

for model in ["barabasi", "erdos"]:

    plt.figure(figsize=(10,6))

    y = results[model]["clustering"]

    plt.plot(
        n_values,
        y,
        marker="o",
        linewidth=2.5,
        color=colors[model],
        label = "Measure Cluster"
    )

    x_log = np.log2(n_values)

    slope, intercept = np.polyfit(
        x_log,
        y,
        1
    )

    fit_y = slope * x_log + intercept

    plt.plot(
        n_values,
        fit_y,
        color="#d62728",
        linestyle="--",
        linewidth=2,
        label=f"Fit (slope={slope:.5f})"
    )

    plt.xscale("log", base=2)
    ax = plt.gca()
    ax.yaxis.set_major_locator(MultipleLocator(0.01))

    plt.xticks(
        n_values,
        [f"2^{i}" for i in range(7,19)],
        rotation=45
    )

    plt.grid(
        True,
        linestyle="--",
        alpha=0.4
    )

    plt.xlabel("Number of Vertices (n)")
    plt.ylabel("Average Clustering Coefficient")

    plt.title(
        f"{names[model]} Clustering Coefficient vs Number of Vertices"
    )
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        f"{model}_clustering_plot.png",
        dpi=300
    )

    plt.close()


# =========================
# DEGREE DISTRIBUTIONS
# =========================

for model in ["barabasi", "erdos"]:

    for n in [1000, 10000, 100000]:

        dist = degree_distributions[model][str(n)]

        x = sorted(map(int, dist.keys()))
        y = [dist[str(k)] if str(k) in dist else dist[k] for k in x]

        # ------------------
        # LIN-LIN
        # ------------------

        plt.figure(figsize=(10,6))

        plt.scatter(
            x,
            y,
            color=colors[model],
            s=25,
            alpha=0.8
        )

        plt.grid(
            True,
            linestyle="--",
            alpha=0.4
        )

        plt.xlabel("Degree")
        plt.ylabel("Number of Vertices")

        plt.title(
            f"{names[model]} Degree Distribution (n={n})"
        )
        plt.legend()
        plt.tight_layout()

        plt.savefig(
            f"{model}_{n}_degree_linlin.png",
            dpi=300
        )

        plt.close()

        # ------------------
        # LOG-LOG
        # ------------------

        filtered = [
            (degree, count)
            for degree, count in zip(x, y)
            if degree > 0 and count > 0
        ]

        x_filtered = [
            degree for degree, count in filtered
        ]

        y_filtered = [
            count for degree, count in filtered
        ]

        plt.figure(figsize=(10,6))

        plt.scatter(
            x_filtered,
            y_filtered,
            color=colors[model],
            s=25,
            alpha=0.8,
            label="Data"
        )

        plt.xscale("log", base=2)
        plt.yscale("log", base=2)

        plt.grid(
            True,
            which="both",
            linestyle="--",
            alpha=0.4
        )

        plt.xlabel("Degree")
        plt.ylabel("Number of Vertices")

        plt.title(
            f"{names[model]} Degree Distribution (n={n})"
        )

        fit_data = [
            (degree, count)
            for degree, count in filtered
            if count >= 5
        ]

        if len(fit_data) >= 2:

            fit_x = np.array([
                degree for degree, count in fit_data
            ])

            fit_y = np.array([
                count for degree, count in fit_data
            ])

            log_x = np.log2(fit_x)
            log_y = np.log2(fit_y)

            slope, intercept = np.polyfit(
                log_x,
                log_y,
                1
            )

            line_x = np.array(
                sorted(x_filtered)
            )

            line_y = 2 ** (
                slope * np.log2(line_x)
                + intercept
            )

            plt.plot(
                line_x,
                line_y,
                color="#d62728",
                linestyle="--",
                linewidth=3,
                label=f"Slope = {slope:.3f}"
            )

            print(
                f"{model} n={n} slope = {slope:.3f}"
            )

        plt.legend()

        plt.tight_layout()

        plt.savefig(
            f"{model}_{n}_degree_loglog.png",
            dpi=300
        )

        plt.close()

print("\nplots finished\n")