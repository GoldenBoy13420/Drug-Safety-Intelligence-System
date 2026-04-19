import pandas as pd
import os

def convert_all_tables(raw_path, processed_path):
    
    tables = ["DEMO", "DRUG", "REAC", "OUTC", "RPSR", "THER", "INDI"]
    quarters = ["Q1", "Q2", "Q3", "Q4"]
    
    for table in tables:
        for q in quarters:
            
            input_file = f"{raw_path}/{table}25{q}.txt"
            output_file = f"{processed_path}/{table}25{q}.csv"
            
            if os.path.exists(input_file):
                txt_to_csv(input_file, output_file)