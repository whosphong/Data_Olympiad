# Building Data Genome Project 2 – Electricity Data Cleaning

This repository contains the data cleaning process for the electricity consumption dataset used in the Building Data Genome Project 2:  
https://github.com/buds-lab/building-data-genome-project-2/tree/master/data

The dataset we worked with is `electricity_cleaned.csv`, which differs from the raw version by treating faulty meter readings (such as zeros) as missing values (`NaN`) rather than valid data points.

The full code used for this stage of the project can be found here:  
https://github.com/whosphong/Data_Olympiad/tree/main/Data%20Cleaning

## Overview

The dataset includes 17544 hourly readings per meter, collected from 2016 to 2018. It covers a total of 19 unique sites across the United States and Europe and consists of 16 unique electricity usage types recorded across buildings at each site.

## Missing Values

A major challenge with the dataset is the presence of missing values from the meter readings. In total, we observed 2471853 missing entries across all meters. To better understand the scale of this issue, we visualized the percentage of missing data for each building per site.

Buildings with 40 percent or more missing data were considered too unreliable for imputation. These buildings were removed from the dataset, resulting in a filtered set of 1455 building locations.

We further screened the data using a weekly rolling window. Any building that had fewer than 120 valid hourly readings in any given week was excluded to ensure temporal consistency. After applying this filter, we retained 734 building meters, each with a complete and reliable time series for the entire two-year period.

## Imputation

For the remaining buildings with some missing values, we used a combination of forward fill and backward fill techniques to impute missing data. This preserves trends in usage while filling in short gaps.

- Forward fill uses the last valid observation to fill the missing value  
- Backward fill uses the next valid observation to fill the missing value

## Anomaly Detection

Anomalies were defined as values falling outside of three standard deviations from a building’s typical usage distribution. We identified 94377 anomalies, many of which lay above the 99.9th percentile and were likely due to meter malfunctions or short-term logging errors.

To clean these anomalies, we replaced them using a 24-hour rolling median. This method helps preserve local patterns while eliminating sudden noise from the dataset. A visualization comparing the original and cleaned readings shows how extreme spikes are smoothed out effectively.

## Outliers

Outliers falling outside the Interquartile Range (IQR) but not classified as anomalies were retained. These may reflect meaningful events, such as equipment usage spikes or occupancy changes, and could provide important context during modeling. These points will be addressed during the modeling phase using techniques like scaling, transformations, or winsorization as appropriate.

## Final Dataset

After cleaning, the final dataset consists of 734 building meters with complete and reliable time series data, each spanning 17544 hourly observations from 2016 to 2018.
