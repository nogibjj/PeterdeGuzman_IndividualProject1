 # This is a README for IDS 706 Individual Project 1

### Status Badges 

### Youtube Video:


### Project Motivation:
This project creates a Python script that utilizes the Pandas package to generate descriptive statistics and the Matplotlib package to produce data visualizations. I also use GitHub Actions to install required packages, lint and format the files, and test both the Python script and Jupyer notebook. 


### Data Used in this Project:
This project uses a subset of voter registration data for Durham County, North Carolina made available by the North Carolina State Board of Elections. This data was downloaded as a zipped file on September 16th, 2024. 

More information and a link to the data is available at: https://www.ncsbe.gov/results-data/voter-registration-data

### Project Directory
```
PeterdeGuzman_IndividualProject1/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       ├── main.yml
├── .pytest_cache
├── .ruff_cache
├── .gitignore
├── main.ipynb
├── main.py
├── Makefile
├── ncvoter89.txt
├── output.png
├── README.md
├── Requirements.txt
└── test_main.py
```




### Functions Created in this Project
    1. read_csv_ncvoterdata() - this function reads in the North Carolina voter registration data, and accounts for both the value of the first row being column names and the raw file being tab-delimited.
    2. mean_age() - this function identifies the age column in the DataFrame and calculates the mean age.
    3. median_age() - this function identifies the age column in the DataFrame and calculates the median age.
    4. std_age() - this function identifies the age column in the DataFrame and calculates the standard deviation of age.
    5. generate_histogram_age() - this function identifies the age column in the DataFrame and createss a histogram to display the age distribution for a sample of registered voters in the county of interest. 
    6. generate_pop_pyramind() 
I also created supplementary test functions in the "test_lib.py" and "test_main.py" scripts to test the operation and output of the created functions. 


### Statistics Summary



|gender_code    | F |     M  |   U |
|Age Group|                      
|18-24 yrs |   11753 |   9734 |  6018 |
|25-29 yrs |  16320 | 12216 | 6039 |
|30-34 yrs |   17805 | 14125 | 5221 |
|35-39 yrs |   15193 | 12721 | 3685 |
|40-44 yrs |   11346 |  9639 | 2381 |
|45-49 yrs |    9127 |  7652 | 1726 |
|50-54 yrs |    8667 |  7390 | 1520 |
|55-59 yrs |    8404 |  7065 | 1316 |
|60-64 yrs |    9047 |  7498 | 1296 |
|65+ yrs   |   34735 | 26378 | 2820 |

### Data Visualizations
To visualize the age distribution of registered voters in Durham County I created a simple histogram. 
![alt text](output_histogram.png)
I also created a population pyramid of registered voters in Durham County that displays the count of registered voters by gender code and age group. As displayed in the above Age Group by Gender table, there are records in this dataset with "Unknown" gender codes, and this visualization does not include those registered voters. 
![alt text](output_age_gender_pyramid.png)


