import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("/data/sensor_data.csv")

# Convert columns
df["Time"] = pd.to_datetime(df["Time"])
df["Temp"] = df["Temp"].astype(float)

# Plot
plt.figure(figsize=(8,4))
plt.plot(df["Time"], df["Temp"], marker="o")
plt.title("Temperature Over Time")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.grid(True)

# Save image
plt.tight_layout()
plt.savefig("/data/temp_chart.png")
plt.close()
