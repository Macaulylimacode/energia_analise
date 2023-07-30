# Importações e Carregamento
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")


class CONFIG:
    NAMES_DTYPES = {"Source": str, "Production": np.float32}


data = pd.read_csv(
    "intermittent.csv",
    index_col="Date and Hour",
    parse_dates=["Date and Hour", "Date"],
    infer_datetime_format=True,
    dtype=CONFIG.NAMES_DTYPES,
)
# EDA rápido
data.info()
data.head(10)


def plotProductionTechnology(technology):
    fig, axes = plt.subplots(5, 1, figsize=(20, 40))
    axes[0].set_title(technology + " Production For Different Granualities", size=20)
    query = data[data["Source"] == technology]
    query["Production"].plot(rot=35, ax=axes[0])
    axes[0].set_xlabel("Hour Granularity", size=15)

    query.groupby("Date").mean(numeric_only=True)["Production"].plot(ax=axes[1])
    axes[1].set_xlabel("Day Granularity", size=15)

    query.groupby("dayName").mean(numeric_only=True)["Production"].plot(ax=axes[2])
    axes[2].set_xlabel("Day Name", size=15)

    query.groupby("dayOfYear").mean(numeric_only=True)["Production"].plot(ax=axes[3])
    axes[3].set_xlabel("Day of Year", size=15)

    query.groupby("monthName").mean(numeric_only=True)["Production"].plot(ax=axes[4])
    axes[4].set_xlabel("Month Name", size=15)

    for i in range(len(axes)):
        axes[i].set_ylabel("Production ($MW$)", size=20)
    plt.show()


plotProductionTechnology(technology="Wind")
plotProductionTechnology(technology="Solar")
