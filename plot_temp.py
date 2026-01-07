import pandas as pd
import matplotlib.pyplot as plt

# Read CSV WITHOUT header
df = pd.read_csv(
    "data/sensor_data.csv",
    header=None,
    names=["Time", "Temperature", "Humidity", "LDR", "AC", "Light"]
)

# Convert Time to datetime
df["Time"] = pd.to_datetime(df["Time"])

# Plot
plt.figure(figsize=(8,4))
plt.plot(df["Time"], df["Temperature"], marker="o")
plt.title("Temperature")
plt.xlabel("Time")
plt.ylabel("°C")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("temp_chart.png")
