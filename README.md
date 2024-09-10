# Impact of Increasing Solar Power Production on Spot Power Market in Central Europe

This repository contains an analysis of how increasing solar power production in Germany has impacted the spot power market prices in Central Europe, particularly focusing on countries like Germany, Czechia, and Slovakia. The analysis compares the daily peak vs. off-peak spot prices and investigates the correlation with solar power production. 

## Key Highlights

- **Objective**: Analyze the correlation between increased solar capacity and power generation in Germany, and its effect on day-ahead spot prices in Central Europe.
- **Data Source**: Data fetched from the ENTSO-E transparency platform using the `entsoe-py` API.

## Repository Structure

- `data/`: Folder to store the datasets. Instructions on how to download data via the API are provided.
- `scripts/`: Python scripts for running the analysis.
- `requirements.txt`: List of dependencies required to run the scripts.
- `LICENSE`: License for the repository.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SimonDataLab/solar-power-market-impact.git
   cd solar-power-market-impact
