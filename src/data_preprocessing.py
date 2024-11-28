from data_ingestion import DataIngestion
from data_transformation import (
    find_constant_column,
    find_columns_with_few_values,
    drop_and_fill
)
from feature_engineering import (
    bin_to_num,
    cat_to_column,
    one_hot_encoding
)
IngestData = DataIngestion("./regression_data/data/cancer_reg.csv")
df = IngestData.load_data()

constant_columns = find_constant_column(df)
print(f"Columns that contains a single or one unique value: {constant_columns}")

threshold = 10
columns_with_few_values = find_columns_with_few_values(df, threshold)
print(f"Columns that contains values less than threshold {threshold} are: {columns_with_few_values}")

df = bin_to_num(df)
df = cat_to_column(df)
df = one_hot_encoding(df)
df = drop_and_fill(df)
print(df.shape)
df.to_csv("regression_data/cancer_reg_processed.csv", index=False)
