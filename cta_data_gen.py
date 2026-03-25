import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
num_days = 60
routes = ["Route A", "Route B", "Route C", "Route D"]

# Generate date range
start_date = datetime(2025, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(num_days)]

# Create data
data = []

for date in dates:
    for route in routes:
        passengers = np.random.randint(50, 300)
        delay = np.random.randint(0, 15)  # delay in minutes
        
        data.append([date.strftime("%Y-%m-%d"), route, passengers, delay])

# Create DataFrame
df = pd.DataFrame(data, columns=["date", "route", "passengers", "delay_minutes"])

# Save to CSV
df.to_csv("cta_ridership_data.csv", index=False)

print("CSV file created: cta_ridership_data.csv")