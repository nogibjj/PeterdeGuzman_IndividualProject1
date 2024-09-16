# Test functions created in main.py script

from main import mean_age, median_age, std_age, generate_histogram_age
import numpy as np
import pandas as pd

num_rows = 10
data = pd.DataFrame(
    {
        "RowID": np.random.randint(0, 101, size=num_rows),
        "age": [18, 19, 21, 25, 35, 40, 45, 45, 55, 65],
    }
)


def test_mean_age():
    result1 = mean_age(data)
    assert result1 == 36.8


def test_median_age():
    result2 = median_age(data)
    assert result2 == 37.5


def test_std_age():
    result3 = std_age(data)
    assert result3 > 16


def test_generate_histogram_age():
    result4 = generate_histogram_age(data)
    assert result4 is None


if __name__ == "__main__":
    test_mean_age()
    test_median_age()
    test_std_age()
    test_generate_histogram_age()
