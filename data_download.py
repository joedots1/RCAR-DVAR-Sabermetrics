from pybaseball import batting_stats, fielding_stats
import pandas as pd

# Define the range of years for analysis
years = range(2014, 2024 + 1)

# Initialize empty lists to store data for each year
batting_data_years = []
fielding_data_years = []

# Pull batting and fielding stats for each year in the range
for year in years:
    # Fetch batting stats for the year and append to list
    batting_data = batting_stats(year, qual = 'n')
    batting_data_years.append(batting_data)
    
    # Fetch fielding stats for the year and append to list
    fielding_data = fielding_stats(year, qual = 'n')
    fielding_data_years.append(fielding_data)

# Concatenate all yearly data into single DataFrames
batting_data_all_years = pd.concat(batting_data_years, ignore_index=True)
fielding_data_all_years = pd.concat(fielding_data_years, ignore_index=True)

# Save combined datasets to CSV files for easy access and review
batting_data_all_years.to_csv('batting_data.csv', index=False)
fielding_data_all_years.to_csv('fielding_data.csv', index=False)
