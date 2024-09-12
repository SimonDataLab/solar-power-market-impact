# Impact of Solar Power Growth on Spot Power Market Prices in Central Europe

This repository explores how the rise in solar power production in Germany has influenced day-ahead spot power prices in Central Europe, with a focus on Germany, Czechia, and Slovakia. The analysis examines the relationship between daily peak and off-peak prices and solar power generation patterns.

**Important Note:** In this analysis, we define "peak" hours as 8 AM to 7:59 PM on all days of the week (including weekends). This differs from the standard industry definition, where peak hours typically refer to the same timeframe but only on weekdays (excluding weekends). We decided to include weekends as the solar production obviously is not impacted by the day of the week.

All data used in this study was sourced from the ENTSO-E transparency platform, and Python code, partially developed with the assistance of ChatGPT, was used to process and analyze the data.

## Key Insights

- **Objective**: Investigate how increased solar capacity in Germany has influenced day-ahead spot power prices in Central Europe, with a special focus on daily peak and off-peak dynamics (Note: "peak" in this analysis refers to 8 AM to 7:59 PM, including weekends).
- **Scope**: Focus on peak vs. off-peak price dynamics across Germany, Czechia, and Slovakia from 2019 to 2024.
- **Data Source**: All data is sourced from the ENTSO-E transparency platform and processed using Python (entsoe-py API).
- **Tools Used**: Python, pandas, matplotlib, and ChatGPT-assisted script development.

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
To run the scripts, you need an API key from ENTSO-E. Replace 'your_api_key_here' in the Python scripts with your own API key. To request this API key (if you already do not have one) , register on the Transparency Platform and send an email to transparency@entsoe.eu with “Restful API access” in the subject line. Indicate the email address you entered during registration in the email body.

## Results

1. **Changes in Peak vs. Off-Peak Price Dynamics (2019-2024)**

   The image below contains four charts:
      1. (chart 1) Historical day-ahead spot power prices.
      2. (charts 2-3) A comparison of prices during the first two weeks of June in 2019 and 2024. It's evident that in 2024, the daytime price "valleys" are much deeper than in 2019, while the highest prices occur just outside of the peak hours (8 AM - 7 PM).
      3. (chart 4) This chart shows the logarithm of absolute values with sign tracking for the ratio of peak to off-peak prices (for more details, refer to the code in market_analysis.py). It illustrates the changing dynamics of peak vs. off-peak prices: during the summer months, peak prices have become significantly lower compared to off-peak prices in recent years. The log-ratio declined from -0.2 in 2023 to -0.4, and further to -0.8 in 2024. This trend correlates with the increase in solar energy production, as shown in the following image. In contrast, the price dynamics during the winter months have remained relatively stable over the past six years. 
![01_market_analysis](https://github.com/user-attachments/assets/a268c2de-e16d-4bd3-8bba-1e6e43ea5db6)
2. **German solar production trend**

   The following charts highlight the rise in solar power generation, especially in 2024. As solar energy, with its low marginal costs, becomes more dominant, its influence on spot market prices is becoming more evident. This is also affecting nearby countries like Czechia and Slovakia due to market coupling and cross-border electricity flows.  
   
![02_solar_capacity_generation](https://github.com/user-attachments/assets/fb2513d9-6749-4125-8528-244c9ec23819)
3. **Further Questions**

   Is the shift in peak vs. off-peak dynamics already reflected in forward base vs. peak pricing? Stay tuned.
