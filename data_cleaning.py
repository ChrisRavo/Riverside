################################
# Function to Clean the DF, returns 
# returns a csv of clean data. 
# 
# C Ravenscroft
# Version 1
#
#
################################
# Requirements
################################
import pandas as pd


################################
# Requirements
################################


import pandas as pd

def remove_duplicates(df):
    """
    Removes duplicate rows based on all columns in the DataFrame.
    
    Parameters:
    - df: DataFrame containing the data.
    
    Returns:
    - DataFrame with duplicates removed, keeping the first occurrence.
    """
    # Check for duplicates across all columns
    if df.duplicated(keep=False).any():
        print("Duplicates found, removing duplicates...")
    else:
        print("No duplicates found.")

    # Remove duplicates, keeping only the first occurrence
    df_cleaned = df.drop_duplicates(keep='first')
    
    return df_cleaned

def delete_rows(df, column_name, value):
    """
    Deletes rows from the DataFrame where the specified column has a specific value.

    Parameters:
    - df: DataFrame containing the data.
    - column_name: The name of the column from which to remove rows.
    - value: The value that will be used to filter rows out.

    Returns:
    - DataFrame with specified rows removed.
    """
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    # Create a new DataFrame excluding the rows where the column has the specified value
    filtered_df = df[df[column_name] != value]
    
    return filtered_df

def delete_nulls(df):
    """
    Deletes rows with null values from the DataFrame.
    
    Parameters:
    - df: DataFrame containing the data.
    
    Returns:
    - DataFrame with nulls removed.
    """
    # Iterate through each column in the DataFrame
    for column in df.columns:
        # Count the number of nulls in the column
        null_count = df[column].isnull().sum()
        print(f"Column '{column}' has {null_count} null(s).")
    
    # Remove rows with any null values
    df_cleaned = df.dropna()

    # Optionally return the cleaned DataFrame
    return df_cleaned

if __name__ == "__main__":
    # Read in the data from the CSV file
    file_path = 'data/InterviewTaskDataFinal.csv'
    df = pd.read_csv(file_path)

    # Remove duplicates based on the unique identifier JOB_NO
    df = remove_duplicates(df)

    # Delete rows where JOB_STATUS is 6 or 90
    df = delete_rows(df, 'JOB_STATUS', 6)
    df = delete_rows(df, 'JOB_STATUS', 90)

    # Remove rows with null values
    df = delete_nulls(df)

    # Save the cleaned DataFrame to a new CSV file
    cleaned_file_path = 'data/data_cleaned.csv'
    df.to_csv(cleaned_file_path, index=False)

    print(f"Cleaned data saved to {cleaned_file_path}.")
