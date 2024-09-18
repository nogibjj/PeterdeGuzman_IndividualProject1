# Test functions created in main.py script

import zipfile

from mylib.lib import (
    read_csv_ncvoterdata,
)
from test_lib import test_generate_histogram_age, test_generate_age_gender_pyramid
import numpy as np
import pandas as pd
from pathlib import Path

file_zip = "ncvoter32.zip"
file_txt = "ncvoter32.txt"


if __name__ == "__main__":
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            df = read_csv_ncvoterdata(f)
    # test_generate_histogram()
    test_generate_histogram_age(df)
    # test_generate_populationpyramid()
    test_generate_age_gender_pyramid(df)

main()


# integration test
# testing that the output files exist
# run main()
# then test out exactly the same way that you tested in the unit test .py file

# create logic to delete the test output plots if they already exist
