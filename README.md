# Impact of Increasing Solar Power Production on Spot Power Market in Central Europe

This repository contains an analysis of how increasing solar power production in Germany has impacted the spot power market prices in Central Europe, particularly focusing on countries like Germany, Czechia, and Slovakia. The analysis compares the daily peak vs. off-peak spot prices (in this analyisis by "peak" we mean 8am - 7pm and "off-peak" 0am - 7am and 8pm - 11pm **for any day - weekend included**) and investigates the correlation with solar power production. 

## Key Highlights

- **Objective**: Analyze the correlation between increased solar capacity and power generation in Germany, and its effect on day-ahead spot prices in Central Europe.
- **Data Source**: Data fetched from the ENTSO-E transparency platform using the `entsoe-py` API.

## Repository Structure

- `scripts/`: Python scripts for running the analysis.
- `requirements.txt`: List of dependencies required to run the scripts.
- `LICENSE`: License for the repository.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SimonDataLab/solar-power-market-impact.git
   cd solar-power-market-impact

2. **Install dependencies: It is recommended to use a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

3. **Set up API Key:**
To run the scripts, you need an API key from ENTSO-E. Replace 'your_api_key_here' in the Python scripts with your own API key.
