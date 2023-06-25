import pandas as pd
import glob
import os

def calculate_hemisphere_ratio(key, file_dict):
    df = pd.read_csv(file_dict[key], sep=';', skiprows=range(1, 11))
    df.rename(columns={'0': 'Value'}, inplace=True)

    # Separate the left and right regions into separate columns
    df['Side'] = df['Data ID'].str.split('_').str[0]
    df['Region'] = df['Data ID'].str.split('_').str[1:].str.join('_')
    df.drop('Data ID', axis=1, inplace=True)

    # Data cleaning
    df = df[~(df['Side'] == 'Brainstem')]
    df = df[~(df['Side'] == 'Corpus')]
    df = df[~(df['Side'] == 'Regional WM recovery coefficients using full mask')]
    df = df[~(df['Side'] == 'Third')]

    # Separating duplicates in different dataframes
    df_1 = df[0:64]
    df_2 = df[64:]

    # Calculate the ratio between the hemispheres
    grouped = df_1.groupby(['Region', 'Side']).sum().reset_index()
    pivoted_1 = grouped.pivot(index='Region', columns='Side', values='Value')
    pivoted_1['Ratio'] = pivoted_1['Left'] / pivoted_1['Right']

    grouped = df_2.groupby(['Region', 'Side']).sum().reset_index()
    pivoted_2 = grouped.pivot(index='Region', columns='Side', values='Value')
    pivoted_2['Ratio'] = pivoted_2['Left'] / pivoted_2['Right']

    concatenated_df = pd.concat([pivoted_1, pivoted_2])
    concatenated_df.to_csv('G:/My Drive/Projetos Python/EANM_Analysis/Results/' + key + '.csv', index=True)

path = 'G:/My Drive/TCR/EANM/*.csv'
csv_files = glob.glob(path)
file_dict = {}
key_list = []

for file_path in csv_files:
    file_name = os.path.basename(file_path)
    key = os.path.splitext(file_name)[0]
    file_dict[key] = file_path
    calculate_hemisphere_ratio(key, file_dict)