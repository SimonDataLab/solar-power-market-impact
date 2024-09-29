import pandas as pd
import matplotlib.pyplot as plt
from entsoe import EntsoePandasClient
import pytz

# Initialize the client
client = EntsoePandasClient(api_key='your api key here')

# Define the bidding zone and time period for both data fetching
zone = 'DE_LU'
start_date = pd.Timestamp('2019-01-01', tz='CET')
end_date = pd.Timestamp('2024-09-28', tz='CET')

# ----- Solar Generation Data (First Chart) -----

# Fetch hourly solar generation data
solar_generation = client.query_generation(zone, start=start_date, end=end_date, psr_type='B16')  # 'B16' is the solar type

# Ensure time is in CET/CEST (Central European Time/Daylight Saving)
solar_generation.index = solar_generation.index.tz_convert('CET')

# ----- Installed Capacity Data (Second Chart) -----

# Define the area and years
area = 'DE_LU'
years = range(2019, 2025)  # 2019 to 2024

# Function to fetch installed generation capacity per year
def fetch_installed_generation_capacity(area, year):
    start = pd.Timestamp(f'{year}-01-01', tz='Europe/Brussels')
    end = pd.Timestamp(f'{year}-12-31', tz='Europe/Brussels')
    return client.query_installed_generation_capacity(area, start=start, end=end)

# Fetch installed capacity data for each year
capacity_data = pd.DataFrame()

for year in years:
    yearly_data = fetch_installed_generation_capacity(area, year)
    yearly_data['Year'] = year
    capacity_data = pd.concat([capacity_data, yearly_data])

# Transpose the data so that production types are columns and 'Year' is the index
capacity_data.reset_index(drop=True, inplace=True)  # Remove timestamp index
capacity_data.set_index('Year', inplace=True)       # Set 'Year' as the index

# Identify the top 8 production types by total installed capacity across all years
top_six_types = capacity_data.sum().nlargest(8).index.tolist()

# ----- Plotting Both Charts in One Figure -----

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# First Subplot: Installed Capacity
# Get the default color cycle from matplotlib
colors = plt.cm.tab10.colors

# Variable to track color for non-solar lines
color_index = 0

for prod_type in top_six_types:
    if prod_type == 'Solar':
        ax1.plot(capacity_data.index, capacity_data[prod_type], label=prod_type, color='orange', linewidth=6)
    else:
        ax1.plot(capacity_data.index, capacity_data[prod_type], label=prod_type, color=colors[color_index], linewidth=3)
        color_index += 1

# Customizing the first plot
ax1.set_title('TOP 8 Production Types by Installed Capacity for Germany (2019-2024)', fontsize=14)
#ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Installed Capacity (MW)', fontsize=12)
ax1.legend(title='Production Type', loc='upper left', fontsize=10)
ax1.grid(True)

# Second Subplot: Solar Generation
ax2.plot(solar_generation.index, solar_generation, color='gold', alpha=0.8, linewidth=0.8, label='Solar Generation (MW)')

# Highlight months from April to September (without adding to the legend)
for year in range(2019, 2025):
    april_start = pd.Timestamp(f'{year}-04-01', tz='CET')
    september_end = pd.Timestamp(f'{year}-09-30', tz='CET')
    ax2.axvspan(april_start, september_end, color='lightgrey', alpha=0.3)

# Customizing the second plot
ax2.set_title('Solar Generation in Germany (2019-2024) with April to September Highlighted')
ax2.set_ylabel('Generation (MW)')
#ax2.set_xlabel('Time')
#ax2.legend()  # Legend will only show 'Solar Generation (MW)' once
ax2.grid(True)

# Tight layout for better spacing between subplots
plt.tight_layout()

# Show the combined plot
plt.show()
