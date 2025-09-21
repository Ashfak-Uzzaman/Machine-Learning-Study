import csv

from tabulate import tabulate

def display_csv_tabulate(filepath):
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        rows = list(reader)
   
        print(tabulate(rows, headers=header, tablefmt="grid")) # You can choose other formats like "pipe", "simple", etc.

import pandas as pd
def tabulate_data(column, X):
    dataframe = pd.DataFrame(X, columns=column)
    print(tabulate(dataframe, headers='keys', tablefmt='grid'))



def display_csv_basic(filepath): 
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Read the header row
        
        # Determine maximum column widths for alignment
        col_widths = [len(col) for col in header]
        for row in reader:
            for i, cell in enumerate(row):
                if i < len(col_widths): # Ensure index is within bounds
                    col_widths[i] = max(col_widths[i], len(cell))
        
        # Reset file pointer to the beginning to read data again
        csvfile.seek(0) 
        reader = csv.reader(csvfile)
        next(reader) # Skip header again

        # Print header
        header_format = " | ".join([f"{{:<{w}}}" for w in col_widths])
        print(header_format.format(*header))
        print("-" * (sum(col_widths) + (len(col_widths) - 1) * 3)) # Separator line

        # Print data rows
        for row in reader:
            print(header_format.format(*row))
            
            


