# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import zipfile


# define functions
def read_csv_ncvoterdata(voterdata):
    return pd.read_csv(
        voterdata, sep="\t", header=0, encoding="unicode_escape", low_memory=False
    )


# define analysis functions


def mean_age(df):
    # calculate mean of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].mean()
        return result
    else:
        result = print("No column containing 'age' found.")
    return result


def median_age(df):
    # calculate median of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].median()
        return result
    else:
        result = print("No column containing 'age' found.")
    return result


def std_age(df):
    # calculate standard deviation of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].std()
        return result
    else:
        result = print("No column containing 'age' found.")
    return result


def recode_age_groups(series):
    if series >= 18 & series <= 24:
        return "18-24 yrs"
    elif 25 <= series <= 29:
        return "25-29 yrs"
    elif 30 <= series <= 34:
        return "30-34 yrs"
    elif 35 <= series <= 39:
        return "35-39 yrs"
    elif 40 <= series <= 44:
        return "40-44 yrs"
    elif 45 <= series <= 49:
        return "45-49 yrs"
    elif 50 <= series <= 54:
        return "50-54 yrs"
    elif 55 <= series <= 59:
        return "55-59 yrs"
    elif 60 <= series <= 64:
        return "60-64 yrs"
    elif 65 <= series:
        return "65+ yrs"


def generate_histogram_age(df):
    age_column = [col for col in df.columns if "age" in col]
    plt.figure(figsize=(10, 6))
    bins = 6
    plt.hist(df[age_column], color="orange", bins=bins, edgecolor="black")
    plt.title("Age Distribution for Registered Voters in Durham County, NC")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{int(x):,}")
    )
    x_ticks = np.arange(0, 110, 10)
    plt.xticks(x_ticks)

    plt.savefig("output.png")
    # plt.show()


def main():
    # load data with zipfile and custom function
    with zipfile.ZipFile("ncvoter32.zip") as z:
        with z.open("ncvoter32.txt") as f:
            df = read_csv_ncvoterdata(f)
    # summary statistics
    print(mean_age(df))
    print(median_age(df))
    print(std_age(df))
    df["Age Group"] = df["age_at_year_end"].apply(recode_age_groups)
    df["Age Group"] = pd.Categorical(
        df["Age Group"],
        categories=[
            "18-24 yrs",
            "25-29 yrs",
            "30-34 yrs",
            "35-39 yrs",
            "40-44 yrs",
            "45-49 yrs",
            "50-54 yrs",
            "55-59 yrs",
            "60-64 yrs",
            "65+ yrs",
        ],
        ordered=True,
    )

    print(df["Age Group"].value_counts(sort=False))
    # generate histogram of age distribution
    # and save to output folder
    generate_histogram_age(df)


main()

# test
import pandas as pd
import zipfile


def read_csv_ncvoterdata(voterdata):
    return pd.read_csv(
        voterdata, sep="\t", header=0, encoding="unicode_escape", low_memory=False
    )


with zipfile.ZipFile("ncvoter32.zip") as z:
    with z.open("ncvoter32.txt") as f:
        df = read_csv_ncvoterdata(f)

column_names = df.columns
print(column_names)


def recode_age_groups(series):
    if 18 <= series <= 24:
        return "18-24 yrs"
    elif 25 <= series <= 29:
        return "25-29 yrs"
    elif 30 <= series <= 34:
        return "30-34 yrs"
    elif 35 <= series <= 39:
        return "35-39 yrs"
    elif 40 <= series <= 44:
        return "40-44 yrs"
    elif 45 <= series <= 49:
        return "45-49 yrs"
    elif 50 <= series <= 54:
        return "50-54 yrs"
    elif 55 <= series <= 59:
        return "55-59 yrs"
    elif 60 <= series <= 64:
        return "60-64 yrs"
    elif 65 <= series:
        return "65+ yrs"


df["Age Group"] = df["age_at_year_end"].apply(recode_age_groups)
print(df["Age Group"].value_counts(sort=False))

df["Age Group"] = pd.Categorical(
    df["Age Group"],
    categories=[
        "18-24 yrs",
        "25-29 yrs",
        "30-34 yrs",
        "35-39 yrs",
        "40-44 yrs",
        "45-49 yrs",
        "50-54 yrs",
        "55-59 yrs",
        "60-64 yrs",
        "65+ yrs",
    ],
    ordered=True,
)

print(df["Age Group"].value_counts(sort=False))
