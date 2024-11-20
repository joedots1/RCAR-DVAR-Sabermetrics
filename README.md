# Evaluating Offensive and Defensive Contributions Above Replacement in Baseball

## Overview

This repository contains all files and resources used for the capstone project **"Evaluating Offensive and Defensive Contributions Above Replacement in Baseball with Custom Sabermetrics"**. The project introduces two custom sabermetric metrics:
1. **Runs Created Above Replacement (RCAR):** Measures offensive contributions relative to a replacement-level player at the same position.
2. **Defensive Value Above Replacement (DVAR):** Measures defensive contributions relative to a replacement-level player at the same position.

These metrics were designed for accessibility, allowing amateur and collegiate teams to equitably evaluate player performance using publicly available MLB data.

---

## File Structure

### Project Files
- **`Evaluating Offensive and Defensive Contributions Above Replacement in Baseball with Custom Sabermetrics.ipynb`**  
  The Jupyter Notebook containing the full analysis, metric calculations, visualizations, and results.

### Data Files
- **`batting_data.csv`**  
  Contains batting statistics for MLB players from 2014 to 2024.

- **`fielding_data.csv`**  
  Contains fielding statistics for MLB players from 2014 to 2024.

### Scripts
- **`data_download.py`**  
  Python script to fetch batting and fielding data using the `pybaseball` library. Saves the data as CSV files for analysis.

  See the [pybaseball documentation](https://github.com/jldbc/pybaseball) for more details.  

### Usage instructions
- Clone the repo: 
    - git clone https://github.com/joedots1/RCAR-DVAR-Sabermetrics/
    - cd RCAR-DVAR-Sabermetrics/
- Install Dependencies
    - pip install -r requirements.txt
- Retrieve Data
    - python data_download.py
- Run the Analysis
    - Evaluating Offensive and Defensive Contributions Above Replacement in Baseball with Custom Sabermetrics.ipynb

### Highlights
**Methodology** 
- Metrics such as RCAR and DVAR were developed using percentile-based thresholds to define replacement-level performance by position.
- Statistical methods (ANOVA and Pearson correlation) were employed to validate metrics.
- Visualizations (boxplots, heatmaps, scatter plots) effectively communicated findings.

**Results**
- RCAR: Showed strong alignment with established benchmarks (e.g., WAR).
- DVAR: Provided insights into defensive contributions but revealed structural biases (e.g., overvaluation of catchers and first basemen).

**Additional Information**
- For a detailed explanation of the project goals, methodology, and findings, refer to the Jupyter Notebook (.ipynb), HTML, or PDF files in this repository.

**License**
- This project is for educational and research purposes only.
Data sourced using the pybaseball library and MLB datasets.

**Contact**
- For any inquiries, please contact the project author.
