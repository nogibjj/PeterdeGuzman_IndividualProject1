import zipfile
import pandas as pd
import matplotlib.pyplot as plt

from mylib.lib import (
    read_csv_ncvoterdata,
    mean_age,
    median_age,
    std_age,
    recode_age_groups,
    make_categorical_agecat,
    generate_histogram_age,
    generate_age_gender_pyramid,
)


# test

file_zip = "ncvoter32.zip"
file_txt = "ncvoter32.txt"
with zipfile.ZipFile(file_zip) as z:
    with z.open(file_txt) as f:
        df = read_csv_ncvoterdata(f)

print(mean_age(df))
print(median_age(df))
print(std_age(df))
print(df["Age Group"].unique())

df["Age Group"] = df["age_at_year_end"].apply(recode_age_groups)
# something about making age group is breaking
print(df["Age Group"].unique())
df = make_categorical_agecat(df)
print(df["Age Group"].unique())

# generate histogram of age distribution
generate_histogram_age(df)
# generate population pyramid of age and gender


# generate_age_gender_pyramid(df)

age_gender_counts = (
    df.groupby(["Age Group", "gender_code"]).size().unstack(fill_value=0)
)
print(age_gender_counts)
age_groups = age_gender_counts.index
print(age_groups)
males = age_gender_counts["M"]
females = age_gender_counts["F"]
print(age_gender_counts)
# Convert males to negative values for plotting
males_negative = -males

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the population pyramid
ax.barh(
    age_groups,
    males_negative,
    color="cornflowerblue",
    label="Male",
    edgecolor="black",
)
ax.barh(age_groups, females, color="salmon", label="Female", edgecolor="black")

# Set labels and title
ax.set_xlabel("Number of Observations")
ax.set_ylabel("Age Groups")
ax.set_title("Registered Voters of Durham County, NC by Gender and Age Group")
ax.legend()

# Add grid for better readability
ax.grid(True)
plt.savefig("output_age_gender_pyramid.png")
plt.show()
