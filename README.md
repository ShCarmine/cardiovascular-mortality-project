# Cardiovascular Mortality Analysis

This project analyzes cardiovascular disease mortality data from Our World in Data, based on the WHO Mortality Database.

## 🫀 Research Question

**Which five countries reported the highest cardiovascular disease death rates in 2020, and how did some of these rates change annually between 2000 and 2020 in countries with complete data?**

## 📊 Dataset

- Source: Our World in Data / WHO Mortality Database
- File used: `cardiovascular-disease-death-rate-who-mdb.csv`

## ⚙️ What the script does

- Loads and prepares the dataset
- Identifies the five countries with the highest cardiovascular disease death rates in 2020
- Calculates mean, standard deviation, skewness, and a subsampling-based estimate of the mean uncertainty
- Analyzes annual mortality changes from 2000 to 2020 for Moldova, Kyrgyzstan and Bulgaria
- Calculates the mean annual percentage change and its variability
- Generates two figures

## 📂 Output

- `Figure_1.png` – Top five countries by cardiovascular disease death rate in 2020
- `Figure_2.png` – Mortality trends from 2000 to 2020 for Moldova, Kyrgyzstan and Bulgaria

## ▶️ How to run

```bash
python "cardiovascular analysis.py"
