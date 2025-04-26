import pandas as pd
path = (r'C:\Users\shrey\Documents\electricity.csv')
df = pd.read_csv(path)
#print(df.head())
timestamp_col = df.columns[0]  # First column = timestamp

cols_to_convert = df.columns.difference([timestamp_col])

for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')
missing_info = df.isnull().sum()
missing_info = missing_info[missing_info > 0]
print(missing_info)

missing_percentage = df.isnull().mean()
cols_50_percent_missing = missing_percentage[missing_percentage >= 0.5]
print(cols_50_percent_missing)
print("Total columns with >= 50% missing values:", len(cols_50_percent_missing))
missing_percentage = df.isnull().mean()
cols_to_remove = missing_percentage[missing_percentage >= 0.5].index.tolist()
df_removed = df[cols_to_remove]     df_kept = df.drop(columns=cols_to_remove)

print("Removed columns (>=50% missing):", cols_to_remove)
print("Number of removed columns:", len(cols_to_remove))
print("New shape of kept DataFrame:", df_kept.shape)
all_zero_cols = df_kept.columns[(df_kept == 0).all()].tolist()
print("Columns where all rows are zero:", all_zero_cols)
print("Total columns where all rows are zero:", len(all_zero_cols))
all_zero_cols = df_kept.columns[(df_kept == 0).all()].tolist()
df_all_zero = df_kept[all_zero_cols]           # DataFrame of all-zero columns
df_final = df_kept.drop(columns=all_zero_cols)  # DataFrame without all-zero columns
print("Columns with all zeros:", all_zero_cols)
print("Number of all-zero columns:", len(all_zero_cols))
print("Shape of final DataFrame (non-all-zero columns):", df_final.shape)
timestamp_col = df_final.columns[0]
print("Timestamp column is:", timestamp_col)
df_final[timestamp_col] = pd.to_datetime(df_final[timestamp_col], errors='coerce')
df_final['Year'] = df_final[timestamp_col].dt.year
df_final['Month'] = df_final[timestamp_col].dt.month
df_final['Date'] = df_final[timestamp_col].dt.date
numeric_cols = df_final.columns.difference([timestamp_col, 'Year', 'Month', 'Date'], sort=False)
df_daily = df_final.groupby('Date')[numeric_cols].sum().reset_index()
df_monthly = df_final.groupby(['Year', 'Month'])[numeric_cols].sum().reset_index()
df_yearly = df_final.groupby('Year')[numeric_cols].sum().reset_index()
save_path = r'C:\Users\shrey\Documents\Data Masters Competition\final_data_splits_by_time_SUM.xlsx'
with pd.ExcelWriter(save_path) as writer:
    df_daily.to_excel(writer, sheet_name='Daily Basis', index=False)
    df_monthly.to_excel(writer, sheet_name='Monthly Basis', index=False)
    df_yearly.to_excel(writer, sheet_name='Yearly Basis', index=False)
print("\nExcel file saved successfully at:", save_path)


