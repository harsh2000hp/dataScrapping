from main import *
import pandas as pd

# Specify the file path for the output file
output_file = 'output.txt'

# Open the file in write mode
with open(output_file, 'w') as file:
    # Write the column names to the file
    file.write('\t'.join(df.columns) + '\n')

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        # Convert each value to a string and join them with tabs
        row_values = '\t'.join([str(value) for value in row])

        # Write the row values to the file
        file.write(row_values + '\n')

# Print a confirmation message
print(f"Data written to {output_file} successfully!")