# solar-power-market-impact
Impact of Increased Solar Power Production in Germany on Spot Power Markets in Central Europe

This project analyzes the impact of increasing solar power production in Germany on spot electricity prices in Central Europe, focusing on how increased solar capacity influences hourly prices during daylight hours compared to night prices. The analysis uses data from ENTSO-E to examine historical trends and demonstrates how higher solar generation in Germany impacts not only German spot prices but also the Czech and Slovak markets due to interconnected grids. The findings can inform power market modeling and highlight potential considerations for forward base and peak product pricing.

## Table of Contents
1. [Data Sources](#data-sources)
2. [Analysis Overview](#analysis-overview)
3. [Key Findings](#key-findings)
4. [Impact on Market Modeling](#impact-on-market-modeling)
5. [Running the Analysis](#running-the-analysis)
6. [Conclusion](#conclusion)

## Data Sources
- **ENTSO-E Transparency Platform**: This project uses generation and spot price data from the ENTSO-E platform, which provides access to electricity market information across Europe.
  - Solar generation data: [ENTSO-E Generation Data](https://transparency.entsoe.eu/)
  - Spot price data: [ENTSO-E Market Data](https://transparency.entsoe.eu/)

## Analysis Overview
The analysis consists of two main parts:
1. **Singnificant changes in Spot Prices**: 
   - The first script downloads historical spot market prices in Germany, the Czech Republic, and Slovakia.
   - We demonstrate that there is visible significant trend in lower spot prices during daylight (peak) hours compared to the nighttime hours (offpeak).
   
2. **Increase in German solar output**:
   - The second script focuses on Germany's growing solar capacity.
   - Due to cross-border flows, increased solar output in Germany leads to price impacts in neighboring countries.

## Key Findings
1. **Lower Daytime Prices**: As Germany increases its solar capacity, daytime prices are consistently lower than nighttime prices due to solar’s low marginal costs.
2. **Impact Beyond Germany**: The interconnected power grids of Central Europe mean that price dynamics in Germany also affect neighboring countries like the Czech Republic and Slovakia.
3. **Modeling Implications**: The difference in daylight and nighttime prices should be considered in forward pricing models for base and peak products. We raise the question of whether these dynamics are fully reflected in current forward curves.

## Impact on Market Modeling
The observed reduction in spot prices during daylight hours due to increased solar generation suggests that:
1. Market participants should account for these dynamics when modeling hourly power forward curves.
2. The divergence between day and night prices may require separate consideration in forward base and peak product pricing.
3. It raises the question: Are current forward curves accurately pricing in these trends? Further investigation is needed to assess how much of the daytime solar impact is already priced into forward contracts, and whether adjustments are required.

