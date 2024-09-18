# import packages
import zipfile

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


def main(file_zip, file_txt):
    # load data with zipfile and custom function
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            df = read_csv_ncvoterdata(f)
    # summary statistics
    print(mean_age(df))
    print(median_age(df))
    print(std_age(df))
    df["Age Group"] = df["age_at_year_end"].apply(recode_age_groups)
    make_categorical_agecat(df)
    # generate histogram of age distribution
    generate_histogram_age(df)
    # generate population pyramid of age and gender
    generate_age_gender_pyramid(df)


file_zip = "ncvoter32.zip"
file_txt = "ncvoter32.txt"
main(file_zip, file_txt)
