# Cardiovascular Mortality Analysis

This project explores a public dataset of cardiovascular disease mortality rates from Our World in Data, based on the WHO Mortality Database.

## 🫀 Research Question

**Which five countries reported the highest cardiovascular disease death rates in 2020, and how did these rates change between 2000 and 2020?**

## 📊 Dataset

- Source: [Our World in Data – Cardiovascular disease death rate](https://ourworldindata.org/grapher/cardiovascular-disease-death-rate-who-mdb)
- Data source: WHO Mortality Database
- File used: `cardiovascular-disease-death-rate-who-mdb.csv`

## ⚙️ What the script does

- Loads and prepares the dataset
- Renames the cardiovascular mortality column as `Death_rate`
- Selects the data available for 2020
- Identifies the top 5 countries with the highest cardiovascular disease death rates
- Calculates:
  - Mean
  - Standard deviation
  - Skewness
  - Estimated uncertainty of the mean using subsampling
- Analyzes the mortality trends of the top 5 countries from 2000 to 2020
- Calculates the percentage change between 2000 and 2020
- Visualizes:
  - Top 5 countries by cardiovascular disease death rate in 2020
  - Cardiovascular mortality trends from 2000 to 2020

## 📂 Output

The script generates:

- `Figure_1.png`
- `Figure_2.png`

## ▶️ How to run

```bash
python "cardiovascular analysis.py"
