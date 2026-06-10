# Bangladesh Road Accident Poisson Analysis

Modelling daily road accidents in Bangladesh using Poisson distribution with 2025 data.

## What This Project Does
- Models daily road accident frequency using Poisson distribution
- Calculates probability of exactly k accidents occurring in a day
- Uses real 2025 data from Bangladesh Passenger Welfare Association

## Key Findings
- Lambda (average daily accidents): 18
- Highest probability at k=17 and k=18 (0.0936 each)
- Distribution approximates Normal due to high lambda (Central Limit Theorem)

## Data Source
Bangladesh Passenger Welfare Association, Annual Road Accident Report 2025
Total accidents in 2025: 6,729 → daily average = 6,729 ÷ 365 ≈ 18

## Limitations
- Data compiled from media reports only . many accidents go unreported
- WHO estimates actual fatalities far higher than official figures
- Poisson assumes accidents are independent .ignores seasonality (Eid, rain, night)
- Daily average smooths out real variation across days
- Not suitable for policy making without BRTA administrative data and hospital records

## Tools Used
- Python (no external libraries)

## Author
Rakibul Hasan Rahim
B.Sc. Statistics, University of Dhaka

GitHub: github.com/Sociallyrakib
