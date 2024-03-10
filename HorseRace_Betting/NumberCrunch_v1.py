import pandas as pd
import openpyxl
import json
import tkinter as tk
from tkinter import filedialog
import datetime as dt


data = [
    ['Extra_innings', 13, 3.9, 62, 151, 29, 42, 105, 21.9,0],
    ['Tee_shot', 29, 11.6, 288, 382, 34, 35, 107, 14.7,0],
    ['Rancho_red', 21, 6.3, 39, 57, 36, 51, 94, 1.8,0]
]

columns = ['Horse', 'Days', 'D/T', 'Race_Freq', 'Dirt_Wins', 'Distance', 'Purse', 'Layoff', 'Mud','Rank']

df = pd.DataFrame(data, columns=columns)
print(df)

def calculate_score(row):
    score = 0
    
    # D/T column score
    dt_max = df['D/T'].max()
    if row['D/T'] == dt_max:
        score += 3
    elif row['D/T'] > dt_max * 0.7:
        score += 2
    else:
        score += 1
    
    # All other columns score (except the first column and "Rank" column)
    for column in df.columns[1:]:
        if column != 'Horse' and column != 'Rank':
            min_val = df[column].min()
            if row[column] == min_val:
                score += 3
            elif row[column] < min_val * 1.3:
                score += 2
            else:
                score += 1
    
    return score

# Apply the function to calculate scores and populate the "Rank" column
df['Rank'] = df.apply(calculate_score, axis=1)
print(df)