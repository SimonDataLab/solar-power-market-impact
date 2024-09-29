import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from entsoe import EntsoePandasClient
import pytz

# Initialize the client with your API key
client = EntsoePandasClient(api_key='your api key here')

# Define the bidding zones
bidding_zones = {
    'DE': 'DE_LU',  # Germany-Luxembourg
    'CZ': 'CZ',     # Czech Republic
    'SK': 'SK'      # Slovakia
}

# Define the time range (CET/CEST)
start = pd.Timestamp('2019-01-01T00:00', tz='CET')
end = pd.Timestamp('2024-09-30T23:59', tz='CET')

# Download day-ahead prices for each bidding zone
prices = {}
for zone, zone_code in bidding_zones.items():
    print(f"Fetching data for {zone}...")
    prices[zone] = client.query_day_ahead_prices(zone_code, start=start, end=end)

# Convert the timezone to CET
for zone in prices:
    prices[zone] = prices[zone].tz_convert('CET')

# Helper function to plot the first 14 days of a given month and year with highlighted peak hours
def plot_first_two_weeks(ax, prices_df, year, label_color):
    # Filter for the first two weeks of the given month and year
    start_date = f'{year}-08-01'
    end_date = f'{year}-08-14'
    first_two_weeks = prices_df[start_date:end_date]
    
    # Plot day-ahead prices for the first two weeks
    ax.plot(first_two_weeks.index, first_two_weeks, label=f'DE Hourly Prices (August 1-14, {year})', color=label_color)
    
    # Highlight peak hours (08:00-19:00) in each day
    for day in pd.date_range(start=start_date, end=end_date, freq='D'):
        peak_start = pd.Timestamp(f'{day.date()} 08:00', tz='CET')
        peak_end = pd.Timestamp(f'{day.date()} 19:00', tz='CET')
        ax.axvspan(peak_start, peak_end, color='orange', alpha=0.2)  # Light orange background for peak hours
    
    ax.set_title(f'DE Day-Ahead Prices for First Two Weeks of August {year} (Highlighting hours 8:00 - 19:59)')
    #ax.set_xlabel('Time')
    ax.set_ylabel('Price (EUR/MWh)')
    ax.grid(True)
    ax.legend()

# Enhanced function: Calculate log-ratios for peak/off-peak and monthly averages
def compute_peak_offpeak_ratios(prices_df):
    # Peak hours: 08:00-19:59, Off-peak hours: 00:00-07:00 and 20:00-23:59
    daily_ratios = pd.DataFrame(index=prices_df.resample('D').mean().index)
    
    peak_hours = prices_df.between_time('08:00', '19:59')
    offpeak_hours_early = prices_df.between_time('00:00', '07:59')
    offpeak_hours_late = prices_df.between_time('20:00', '23:59')
    
    # Combine off-peak hours into a single dataframe
    offpeak_hours = pd.concat([offpeak_hours_early, offpeak_hours_late])
    
    daily_peak = peak_hours.resample('D').mean()
    daily_offpeak = offpeak_hours.resample('D').mean()

    # Calculate the sign of the ratio: If both are negative, the sign is positive; if one is negative, it's negative
    sign_of_ratio = np.sign(daily_peak / daily_offpeak)

    # Calculate the logarithm of the absolute value of the ratio
    log_abs_ratio = np.log(np.abs(daily_peak / daily_offpeak))

    # Multiply the log of absolute value by the sign to restore the original sign of the ratio
    daily_ratios['Log Peak/Off-Peak'] = sign_of_ratio * log_abs_ratio
    
    # Calculate monthly averages (ignores NaN values by default)
    monthly_ratios = daily_ratios.resample('M').mean()
    
    return daily_ratios, monthly_ratios


# Initialize dictionaries to store daily and monthly ratios
ratios = {}
monthly_averages = {}

# Calculate the ratios for all three markets
for zone in prices:
    print(f"Calculating log-ratios for {zone}...")
    daily, monthly = compute_peak_offpeak_ratios(prices[zone])
    ratios[zone] = daily
    monthly_averages[zone] = monthly

# (2) Plot the four charts in one figure
# We use gridspec_kw to specify height ratios: The second and third charts will have smaller heights
fig, axs = plt.subplots(4, 1, figsize=(12, 20), gridspec_kw={'height_ratios': [2, 1, 1, 2]})

# First plot: Hourly day-ahead prices for all three bidding zones
for zone in prices:
    axs[0].plot(prices[zone], label=zone)
axs[0].set_title('Hourly Day-Ahead Power Prices (2019-01-01 to 2024-08-31)')
#axs[0].set_xlabel('Time')
axs[0].set_ylabel('Price (EUR/MWh)')
axs[0].legend()
axs[0].grid(True)

# Second plot: DE hourly prices for the first two weeks of August 2019, highlighting peak hours
plot_first_two_weeks(axs[1], prices['DE'], 2019, 'green')

# Third plot: DE hourly prices for the first two weeks of August 2024, highlighting peak hours
plot_first_two_weeks(axs[2], prices['DE'], 2024, 'blue')

# Fourth plot: Monthly average log peak/off-peak ratios for three markets
for zone in monthly_averages:
    axs[3].plot(monthly_averages[zone].index, monthly_averages[zone]['Log Peak/Off-Peak'], label=f'{zone}')
axs[3].axhline(y=0, color='red', linewidth=2)  # y=0 line for log-ratios
for year in range(2019, 2025):
    start_highlight = pd.Timestamp(f'{year}-04-01')
    end_highlight = pd.Timestamp(f'{year}-09-30')
    axs[3].axvspan(start_highlight, end_highlight, color='lightgray', alpha=0.3)
axs[3].set_title('Monthly Average Log Peak-to-Off-Peak Price Ratios (2019-01-01 to 2024-08-31)')
#axs[3].set_xlabel('Time')
axs[3].set_ylabel('Log Ratio (Peak/Off-Peak)')
axs[3].legend()
axs[3].grid(True)

# Adjust layout: Increase padding between subplots
plt.tight_layout(pad=3.0)

# Show the plots
plt.show()
