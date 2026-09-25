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
    print(f"Model R2: {model.score(x, y)}")
    print(f"Model slope: {model.coef_[0]}")

    min_year = int(min(x)[0])
    max_year = max(x)[0]

    lin_x = np.array([min_year, max_year])
    lin_y = model.predict(lin_x.reshape((-1, 1)))

    # Show  scatterplot of the entire timeseries
    df.plot.scatter(x="Year", y="Decimal Day of Year", c='black')
    plt.plot(lin_x, lin_y, 'b-')

    # Now compute a regression for the 50 years since NSIDC was founded
    x = df[df.Year >= 1976].Year.values.reshape((-1, 1))
    y = df[df.Year >= 1976]["Decimal Day of Year"].values
    model = LinearRegression().fit(x, y)
    print(f"Model R2 (1976-2026): {model.score(x, y)}")
    print(f"Model slope (1976-2026): {model.coef_[0]}")

    lin_x_50years = np.array([1976, 2026])
    lin_y_50years = model.predict(lin_x.reshape((-1, 1)))

    plt.plot(lin_x_50years, lin_y_50years, 'g-')

    plt.axvline(x=1976, color="gold", label="1976")
    plt.title(f"Tanana river breakup dates {min_year}-{max_year}")
    plt.tight_layout()
    plt.savefig(THIS_DIR / "../plots/tannana_river_full_ts.png")



    # Filter to just the last 50 years
    # df[df.Year >= 1976].plot.scatter(x="Year", y="Decimal Day of Year")

    # breakpoint()
