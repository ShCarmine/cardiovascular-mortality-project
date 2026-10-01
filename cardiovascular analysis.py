#Which are the top five countries with the highest cardiovascular disease death rates in 2020?
#How have cardiovascular disease death rates changed over time in these five countries?

#Research question 1:
#Which are the top five countries with the highest cardiovascular disease death rates in 2020?
# Load the dataset
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("cardiovascular-disease-death-rate-who-mdb.csv")
print(data.head())

# Rename the cardiovascular mortality-rate column
data = data.rename(
    columns={
        "Age-standardized deaths that are from cardiovascular diseases per 100,000 people, in both sexes aged all ages": "Death_rate"})

# Select the year 2020
data_2020 = data[data["Year"] == 2020]
print(data_2020.head())

# Sort by cardiovascular disease death rate
# from highest to lowest
top_5 = data_2020.sort_values(
    by="Death_rate",
    ascending=False
).head(5)

# Display only country and death rate
print(top_5[["Entity", "Death_rate"]])

# Graph 1
import matplotlib.pyplot as plt

plt.bar(top_5["Entity"], 
        top_5["Death_rate"], 
        color=["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple"])
plt.xlabel("Country")
plt.ylabel("Deaths per 100,000 people")
plt.title("Top 5 countries by cardiovascular disease death rate in 2020")

for i, value in enumerate(top_5["Death_rate"]):
    plt.text(i, value + 5, f"{value:.1f}", ha="center")

plt.savefig("Figure_1.png", bbox_inches="tight")
plt.show()

#Statistical analysis of all countries in 2020
rates_2020 = data_2020["Death_rate"]

mean_rate = rates_2020.mean()

std_rate = rates_2020.std(ddof=0)

skewness = (((rates_2020 - mean_rate) / std_rate) ** 3).mean()

print(f"Mean: {mean_rate:.2f}")
print(f"Standard deviation: {std_rate:.2f}")
print(f"Skewness: {skewness:.2f}")

# Estimation of Mean Uncertainty

# Randomly shuffle the 2020 death rates
shuffled_rates = rates_2020.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Divide the data into 10 subsamples
subsamples = np.array_split(shuffled_rates, 10)

# Calculate the mean of each subsample
subsample_means = [np.mean(subsample) for subsample in subsamples]

# Calculate the uncertainty as the standard deviation of the subsample means
mean_uncertainty = np.std(subsample_means)

# Print the result
print(f"Mean: {mean_rate:.2f}")
print(f"Uncertainty: {mean_uncertainty:.2f}")

#Research question 2:
#How have cardiovascular disease death rates changed over time in these five countries?

# Create a list with the names of the top 5 countries
top_5_countries = top_5["Entity"].tolist()

# Select all the data for the top 5 countries
top_5_over_time = data[
    data["Entity"].isin(top_5_countries)]

# Select only the years from 2000 to 2020
recent_data = top_5_over_time[
    (top_5_over_time["Year"] >= 2000) &
    (top_5_over_time["Year"] <= 2020)]

# Repeat the analysis for each country
for country in top_5_countries:

    # Select the data for one country
    country_data = recent_data[
        recent_data["Entity"] == country]

    # Plot the death rate over time
    plt.plot(
        country_data["Year"],
        country_data["Death_rate"],
        label=country)

# Graph 2
plt.xlabel("Year")
plt.ylabel("Deaths per 100,000 people")
plt.title("Cardiovascular disease death rates from 2000 to 2020")
plt.legend()
plt.grid()

plt.savefig("Figure_2.png", bbox_inches="tight")
plt.show()