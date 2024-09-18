# Testing Created Functions with Dataset
# Import Packages
import pandas as pd
import zipfile
import os

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

# Declaring Standard Columns for NC voter file data:
List_Match = [
    "county_id",
    "county_desc",
    "voter_reg_num",
    "ncid",
    "last_name",
    "first_name",
    "middle_name",
    "name_suffix_lbl",
    "status_cd",
    "voter_status_desc",
    "reason_cd",
    "voter_status_reason_desc",
    "res_street_address",
    "res_city_desc",
    "state_cd",
    "zip_code",
    "mail_addr1",
    "mail_addr2",
    "mail_addr3",
    "mail_addr4",
    "mail_city",
    "mail_state",
    "mail_zipcode",
    "full_phone_number",
    "confidential_ind",
    "registr_dt",
    "race_code",
    "ethnic_code",
    "party_cd",
    "gender_code",
    "birth_year",
    "age_at_year_end",
    "birth_state",
    "drivers_lic",
    "precinct_abbrv",
    "precinct_desc",
    "municipality_abbrv",
    "municipality_desc",
    "ward_abbrv",
    "ward_desc",
    "cong_dist_abbrv",
    "super_court_abbrv",
    "judic_dist_abbrv",
    "nc_senate_abbrv",
    "nc_house_abbrv",
    "county_commiss_abbrv",
    "county_commiss_desc",
    "township_abbrv",
    "township_desc",
    "school_dist_abbrv",
    "school_dist_desc",
    "fire_dist_abbrv",
    "fire_dist_desc",
    "water_dist_abbrv",
    "water_dist_desc",
    "sewer_dist_abbrv",
    "sewer_dist_desc",
    "sanit_dist_abbrv",
    "sanit_dist_desc",
    "rescue_dist_abbrv",
    "rescue_dist_desc",
    "munic_dist_abbrv",
    "munic_dist_desc",
    "dist_1_abbrv",
    "dist_1_desc",
    "vtd_abbrv",
    "vtd_desc",
]

# Test Data is Tyrell County, NC Voter File Data, which has been independently analyzed
# to verify summary statistics and age distribution.

# Testing Reading Other County NC Voter File Data
file_zip = "ncvoter89.zip"
file_txt = "ncvoter89.txt"

### Loading Data and Testing that there are a standard number of columns for NC voter file data
def test_read_csv_ncvoterdata(file_txt):
    test_df = pd.read_csv(
        file_txt, sep="\t", header=0, encoding="unicode_escape", low_memory=False
    )
    assert test_df is not None
    assert all([col in test_df.columns for col in List_Match])

with zipfile.ZipFile(file_zip) as z:
    with z.open(file_txt) as f:
        df = read_csv_ncvoterdata(f)

# Test Analysis Functions
def test_mean_age(df):
    mean_test = mean_age(df)
    assert mean_test == #value of test data


def test_median_age(df):
   median_test = median_age(df)
   assert median_test == # value of test data

def test_std_age(df):
    std_test = std_age(df)
    assert std_test == # value of test data
    

# Test Recoding Functions
def test_recode_age_groups(series):
    df["Age Group"] = df["age_at_year_end"].apply(recode_age_groups)
    age_cat = [
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
        ]
    unique_values = df["Age Group"].unique()
    all_in_list = all(value in age_cat for value in unique_values)
    print("All unique values in the Series are in the list of defined Age Group categories:", all_in_list)

def test_make_categorical_agecat(df):
    agecat_order = [
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
        ]
    make_categorical_agecat(df)
    df.assertTrue(pd.api.types.is_categorical_dtype(df['Age Group']))
    df.assertListEqual(list(df['Age Group'].cat.categories), agecat_order)

# Test Visualization Functions
def test_generate_histogram_age(df):
    plot_name = "test_histogram"
    generate_age_gender_pyramid(df, plot_name)
    file_path = os.path.join('Output Images', plot_name)
    df.assertTrue(os.path.isfile(file_path), f"{file_path} does not exist.")

def test_generate_age_gender_pyramid(df):
    plot_name = "test_populationpyramid"
    generate_age_gender_pyramid(df, plot_name)
    file_path = os.path.join('Output Images', plot_name)
    df.assertTrue(os.path.isfile(file_path), f"{file_path} does not exist.")
