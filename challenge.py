import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings
from flask import Flask, request, jsonify
import math

warnings.filterwarnings("ignore")

# Load the data
df = pd.read_csv("monatszahlen2505_verkehrsunfaelle_06_06_25.csv")

# Rename columns
df = df.rename(columns={
    'MONATSZAHL': 'Category',
    'AUSPRAEGUNG': 'Type',
    'JAHR': 'Year',
    'MONAT': 'Month',
    'WERT': 'Value'
})

# Clean data
df['Month'] = df['Month'].astype(str)
df = df[~df['Month'].str.strip().str.lower().eq('summe')]
df['Month'] = df['Month'].str[-2:].astype(int)
df = df[df['Year'] <= 2020]

# Filter for Alkoholunfälle & insgesamt
filtered_df = df[(df['Category'] == 'Alkoholunfälle') & (df['Type'] == 'insgesamt')].copy()

# Create datetime column
filtered_df['ds'] = pd.to_datetime(
    filtered_df['Year'].astype(str) + '-' + filtered_df['Month'].astype(str).str.zfill(2) + '-01'
)
filtered_df['y'] = filtered_df['Value']
filtered_df = filtered_df.sort_values('ds')
filtered_df.set_index('ds', inplace=True)

# Plot historical data 
plt.figure(figsize=(12, 6))
plt.plot(filtered_df.index, filtered_df['Value'], marker='o')
plt.title('Historical number of Alkoholunfälle (insgesamt)')
plt.xlabel('Date')
plt.ylabel('Number of accidents')
plt.grid(True)
plt.show()

# Build ARIMA model
ts = filtered_df['Value']
model = ARIMA(ts, order=(1,1,1))
model_fit = model.fit()