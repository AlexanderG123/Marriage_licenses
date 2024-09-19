import pandas as pd

# Load the data from the saved CSV file
data_path = 'data/analysis_data/simulated_marriage_data.csv'
df = pd.read_csv(data_path)

# Test 1: Check Column Names
def test_column_names(df):
    expected_columns = ['_id', 'CIVIC_CENTRE', 'MARRIAGE_LICENSES', 'TIME_PERIOD']
    assert list(df.columns) == expected_columns, f"Expected columns: {expected_columns}, but got: {list(df.columns)}"
    print("Test 1 passed: Column names are correct.")

# Test 2: Validate Civic Centres and Marriage Licenses
def test_civic_centres_and_licenses(df):
    valid_civic_centres = ['ET', 'NY', 'SC', 'TO', 'YK']
    assert df['CIVIC_CENTRE'].isin(valid_civic_centres).all(), "Invalid Civic Centre value found"
    assert (df['MARRIAGE_LICENSES'] >= 0).all(), "Negative number of marriage licenses found"
    print("Test 2 passed: Civic centres and marriage license numbers are valid.")

# Run the tests
test_column_names(df)
test_civic_centres_and_licenses(df)