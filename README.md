# Impact of Increasing Solar Power Production on Spot Power Market in Central Europe

This repository contains an analysis of how increasing solar power production in Germany has impacted the spot power market prices in Central Europe, particularly focusing on countries like Germany, Czechia, and Slovakia. The analysis compares the daily peak vs. off-peak spot prices (in this analyisis by "peak" we mean 8am - 7pm and "off-peak" 0am - 7am and 8pm - 11pm **for any day - weekend included**) and investigates the correlation with solar power production. All the data was downloaded from ENTSO-E transparency platform. ChatGPT was used to help transform my thoughts into python code. 

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
To run the scripts, you need an API key from ENTSO-E. Replace 'your_api_key_here' in the Python scripts with your own API key. To request this API key (if you already do not have one) , register on the Transparency Platform and send an email to transparency@entsoe.eu with “Restful API access” in the subject line. Indicate the email address you entered during registration in the email body.

## Results

1. **How peak-offpeak price dynamics changed over last 6 years?**

   The image below contains four charts:
      1. (chart 1) Historical day-ahead spot power prices.
      2. (charts 2-3) A comparison of prices during the first two weeks of June in 2019 and 2024. It's evident that in 2024, the daytime price "valleys" are much deeper than in 2019, while the highest prices occur just outside of the peak hours (8 AM - 7 PM).
      3. (chart 4) This chart shows the logarithm of absolute values with sign tracking for the ratio of peak to off-peak prices (for more details, refer to the code in market_analysis.py). It illustrates the changing dynamics of peak vs. off-peak prices: during the summer months, peak prices have become significantly lower compared to off-peak prices in recent years. The log-ratio declined from -0.2 in 2023 to -0.4, and further to -0.8 in 2024. This trend correlates with the increase in solar energy production, as shown in the following image. In contrast, the price dynamics during the winter months have remained relatively stable over the past six years. 
![01_market_analysis](https://github.com/user-attachments/assets/a268c2de-e16d-4bd3-8bba-1e6e43ea5db6)
2. **German solar production trend**

   These two charts compare different types of electricity generation in Germany, highlighting the sharper increase in solar power in 2024. This is likely the primary driver of the changes in peak vs. off-peak price dynamics in central Europe, as solar generation has relatively low marginal costs. Czechia and Slovakia are also impacted due to market coupling and strong cross-border energy flows.  
   
![02_solar_capacity_generation](https://github.com/user-attachments/assets/fb2513d9-6749-4125-8528-244c9ec23819)
3. **This leads to another question.**

   Is this dynamics already transformed in forward base vs. peak products pricing? Stay tuned.
