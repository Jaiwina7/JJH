import pandas as pd
import numpy as np

# Number of samples (you can change it later)
n_samples = 500

# Simulate features (random values between chosen ranges)
data = {
    "qber": np.random.uniform(0.01, 0.1, n_samples),
    "channel_loss": np.random.uniform(0.1, 0.5, n_samples),
    "photon_rate": np.random.uniform(500000, 2000000, n_samples),
    "interference": np.random.uniform(0.0, 0.6, n_samples),
    "temperature": np.random.uniform(15, 35, n_samples),
    "previous_qber": np.random.uniform(0.01, 0.09, n_samples),
    "snr": np.random.uniform(10, 40, n_samples)
}

df = pd.DataFrame(data)

# Label the noise level (High = 1, Low = 0)
df["NoiseLabel"] = np.where(
    (df["qber"] > 0.05) | (df["channel_loss"] > 0.3) | (df["interference"] > 0.4),
    1,  # High noise
    0   # Low noise
)

# Save dataset to CSV
df.to_csv("quantum_channel_data.csv", index=False)

print("✅ Synthetic quantum channel dataset created successfully!")
print(df.head())
