import pandas as pd

# Assuming your Excel file is named 'your_file.xlsx' and the sheet is named 'Sheet1'
file_path = 'data/data.xlsx'
sheet_name = 'Sheet1'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)
# Filter rows containing 'guntur' in specific columns
filtered_df = df[df['District Name'].str.contains('guntur', case=False)]
selected_columns = ['First Name (మొదటి పేరు)', 'Contact number (మొబైల్ నంబర్)', 'District Name']
selected_df = filtered_df[selected_columns]


# # # Save the filtered DataFrame to a new Excel file
selected_df.to_excel('output.xlsx', index=False)
