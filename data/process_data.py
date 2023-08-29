import sys
import pandas as pd
import numpy as np
import os
import re
import pickle
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    messages = pd.read_csv (messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on='id')
    return df


def clean_data(df):
    categories = df['categories'].str.split(';', expand=True)
    row = categories.iloc[0]
    category_colnames = row.apply(lambda x: x[:-2])
    categories.columns = category_colnames
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1].astype(int)
        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column], errors = 'coerce')
    df = df.drop(['categories'], axis = 1)
    df = pd.concat([df, categories], axis = 1)
    # Specify the columns to exclude
    exclude_columns = ['id', 'message', 'original', 'genre']
    # Select columns to change the data type
    columns_to_change = df.columns[~df.columns.isin(exclude_columns)]
    # Change the data type of selected columns
    df[columns_to_change] = df[columns_to_change].fillna(99999)
    df[columns_to_change] = df[columns_to_change].astype(int)
    # Search for rows where any column has value == 99999
    rows_to_remove = df[df.eq(99999).any(axis=1)].index
    # Remove the rows
    df.drop(rows_to_remove, inplace=True)
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset=['message']) 
    # drop attribute child_alone
    df = df.drop('child_alone', axis = 1)
    df = df[df.related != 2]
    return df


def save_data(df, database_filename):
    engine = create_engine('sqlite:///'+database_filename)
    df.to_sql('Categories', engine, index=False, if_exists = 'replace')



def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()