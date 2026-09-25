"""Plot Tannana River breakup dates over time.

Data from: https://nsidc.org/data/nsidc-0064/versions/2

Assumes user has downloaded the `NenanaIceClassic_1917-2026.csv` and placed it
into ../data/.
"""
from pathlib import Path

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

THIS_DIR = Path(__file__).parent


if __name__ == "__main__":
    df = pd.read_csv(THIS_DIR / "../data/NenanaIceClassic_1917-2026.csv")

    # compute a linear regression model for the data:
    x = df.Year.values.reshape((-1, 1))
    y = df["Decimal Day of Year"].values
    model = LinearRegression().fit(x, y)
    model_score = model.score(x, y)
    model_slope = model.coef_[0]
    print(f"Model R²: {model_score}")
    print(f"Model slope: {model_slope}")

    min_year = int(min(x)[0])
    max_year = max(x)[0]

    lin_x = np.array([min_year, max_year])
    lin_y = model.predict(lin_x.reshape((-1, 1)))

    plt.figure(figsize=(12, 10))

    # Show  scatterplot of the entire timeseries
    ax = df.plot.scatter(x="Year", y="Decimal Day of Year", c='black')

    plt.plot(lin_x, lin_y, 'b-', label=f"Linear regression (R²: {model_score:.3f}; Slope: {model_slope:.3f})")

    # Now compute a regression for the 50 years since NSIDC was founded
    x = df[df.Year >= 1976].Year.values.reshape((-1, 1))
    y = df[df.Year >= 1976]["Decimal Day of Year"].values
    model = LinearRegression().fit(x, y)
    model_score = model.score(x, y)
    model_slope = model.coef_[0]
    print(f"Model R² (1976-2026): {model_score}")
    print(f"Model slope (1976-2026): {model_slope}")

    lin_x_50years = np.array([1976, 2026])
    lin_y_50years = model.predict(lin_x.reshape((-1, 1)))

    plt.plot(lin_x_50years, lin_y_50years, 'g-', label=f"Linear regression 1976-2026 (R²: {model_score:.3f}; Slope: {model_slope:.3f})")

    plt.axvline(x=1976, color="gold")
    plt.title(f"Tanana river breakup dates {min_year}-{max_year}")
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15))
    plt.tight_layout()
    plt.savefig(THIS_DIR / "../plots/tannana_river_full_ts.png")
