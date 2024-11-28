from data_ingestion import DataIngestion
import pandas as pd
from sklearn.model_selection import train_test_split as tts


def find_constant_column(dataframe) -> list:
    """
    This function takes dataframe as a parameter and return a list of columns having single value or one unique value.

    :Param dataframe (pandas.DataFrame): The datframe which we have to analyze
    :return list: A list of columns that contains a single value 
    """

    const_column = []
    for column in dataframe.columns:
        #Get the unique values in a column
        unique_value = dataframe[column].unique()
        #Check whether a column contains one unique value or not
        if len(unique_value) == 1:
            const_column.append(column)
    return const_column

def delete_constant_columns(dataframe, columns_to_delete) ->pd.DataFrame:
    """
    This function takes the dataframe and the list of columns having single value and return modified version of dataframe by deleting that columns.

    :Param dataframe (pandas.DataFrame): The DataFrame to be analyzed
    :Param columns_to_delete (list): A list of columns having single value to be deleted.
    :return pandas.DataFrame: The Datafrane containing columns having two or more unique values.
    """
    dataframe = dataframe.drop(columns_to_delete, axis=1)
    return dataframe

def find_columns_with_few_values(datframe, threshold) -> list:
    """
    This function takes the dataframe and threshold value and return the columns that have unique values less than threshold

    :Param dataframe (Pandas DataFrame): The dataframe to be analyze
    :Param threshold (int): Minimum number of unique values required for columns
    :return list: A list of columns that have unique values less than threshold
    """

    few_values_columns = []
    for column in datframe.columns:
        #Get the number of unique values in a column
        unique_values = datframe[column].unique()
        #Check whether a column has less than the threshold number of unique value or not
        if len(unique_values) < threshold:
            few_values_columns.append(column)
    return few_values_columns

def find_duplicate_rows(dataframe) -> pd.DataFrame:
    """
    This function takes dataframe as an input and returned the datagrame having duplicate rows.

    :Param dataframe: The DataFrame to be analyzed
    :return pandas.DataFrame: The DataFrame containing duplicated rows
    """
    duplicate_rows = dataframe[dataframe.duplicated()]
    return duplicate_rows

def delete_duplicate_rows(dataframe):
    """
    This function takes dataframe as input and delete the duplicated rows
    :Param dataframe (pandas.DataFrame): The DataFrame to be analyzed
    :return pandas.DataFrame: The DataFrame without duplicated rows
    """
    dataframe = dataframe.drop_duplicate(key = "first")
    return dataframe

def drop_and_fill(dataframe) -> pd.DataFrame:
    """
    This function takes dataframe as input and drop the columns more than 50% missing values
    :Param dataframe (pandas.DataFrame): The DataFrame to be analyzed
    :return pandas.DataFrame: The DataFrame after dropping columns more than 50% null values
    """

    columns_to_drop = dataframe.columns[dataframe.isnull().mean() > 0.5]
    #Drop the columns
    dataframe = dataframe.drop(columns_to_drop, axis = 1)
    #Fill the remaining missing values with the mean of the column
    dataframe = dataframe.fillna(dataframe.mean())
    return dataframe