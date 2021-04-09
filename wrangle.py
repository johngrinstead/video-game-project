import pandas as pd
import numpy as np
import os

# acquire
from env import host, user, password
from pydataset import data
from datetime import date 
from scipy import stats

# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

import sklearn

from sklearn.model_selection import train_test_split

# Wrangle Data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def wrangle_video_games():
    
    # acquire data
    df = pd.read_csv('video_game.csv')
    
    # drop columns with too many unique values
    df = df.drop(columns = ['Name', 'Publisher', 'Developer'])
    
    # drop columns with too many nulls
    df = df.drop(columns = 'User_Count')
    
    ## Drop rows with nulls
    # Clean up release year
    indexYear_of_Release = df.loc[df['Year_of_Release'].isnull()].index 
    df.drop(indexYear_of_Release, inplace=True)
    
    # Clean up Genre
    indexGenre = df.loc[df['Genre'].isnull()].index 
    df.drop(indexGenre, inplace=True)
    
    # Clean up Critic Score
    indexCritic_Score = df.loc[df['Critic_Score'].isnull()].index 
    df.drop(indexCritic_Score, inplace=True)
    
    # Clean up Critic Count
    indexCritic_Count = df.loc[df['Critic_Count'].isnull()].index 
    df.drop(indexCritic_Count, inplace=True)
    
    # Clean up User Score
    indexUser_Score = df.loc[df['User_Score'].isnull()].index 
    df.drop(indexUser_Score, inplace=True)
    
    # Clean up Rating
    indexRating = df.loc[df['Rating'].isnull()].index 
    df.drop(indexRating, inplace=True)
    
    #convert year to int
    df['Year_of_Release'] = df['Year_of_Release'].astype(int)
    
    # repalce tbd with nan
    df = df.replace(to_replace ="tbd",
                 value = np.nan)
    
    #convert user score to float
    df['User_Score'] = df['User_Score'].astype(float)
    User_Score_mean = round(df.User_Score.mean(), 1)
    df['User_Score'] = df['User_Score'].fillna(User_Score_mean)
    
    ## Columns to look for outliers
    # NA_sales
    df = df[df.NA_Sales < 2]
    
    # EU_sales
    df = df[df.EU_Sales < 1]
    
    # JP_sales
    df = df[df.JP_Sales < .4]
    
    # Other_sales
    df = df[df.Other_Sales < 1]
    
    # Global_sales
    df = df[df.Global_Sales < 6]
    
    
    ## make dummy variables for objects
    # dummy platform
    dummy_df = pd.get_dummies(df['Platform'])
    df = pd.concat([df, dummy_df], axis=1)
    
    # dummy genre
    dummy_df = pd.get_dummies(df['Genre'])
    df = pd.concat([df, dummy_df], axis=1)
    
    
    # dummy rating
    dummy_df = pd.get_dummies(df['Rating'])
    df = pd.concat([df, dummy_df], axis=1)
    
    return df

# Split Data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def split(df, stratify_by= None):
    """
    Crude train, validate, test split
    To stratify, send in a column name
    """
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.2, random_state=319)
        train, validate = train_test_split(train, test_size=.3, random_state=319)
    else:
        train, test = train_test_split(df, test_size=.2, random_state=319, stratify=df[stratify_by])
        train, validate = train_test_split(train, test_size=.3, random_state=319, stratify=train[stratify_by])
    return train, validate, test

# Seperate y ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def seperate_y(train, validate, test):
    '''
    This function will take the train, validate, and test dataframes and seperate the target variable into its
    own panda series
    '''
    
    X_train = train.drop(columns=['Critic_Score'])
    y_train = train.Critic_Score
    X_validate = validate.drop(columns=['Critic_Score'])
    y_validate = validate.Critic_Score
    X_test = test.drop(columns=['Critic_Score'])
    y_test = test.Critic_Score
    return X_train, y_train, X_validate, y_validate, X_test, y_test

# Scale Data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def scale_data(X_train, X_validate, X_test):
    '''
    This function will scale numeric data using Min Max transform after 
    it has already been split into train, validate, and test.
    '''
    
    
    obj_col = ['Platform', 'Genre', 'Rating']
    num_train = X_train.drop(columns = obj_col)
    num_validate = X_validate.drop(columns = obj_col)
    num_test = X_test.drop(columns = obj_col)
    
    
    # Make the thing
    scaler = sklearn.preprocessing.MinMaxScaler()
    
   
    # we only .fit on the training data
    scaler.fit(num_train)
    train_scaled = scaler.transform(num_train)
    validate_scaled = scaler.transform(num_validate)
    test_scaled = scaler.transform(num_test)
    
    # turn the numpy arrays into dataframes
    train_scaled = pd.DataFrame(train_scaled, columns=num_train.columns)
    validate_scaled = pd.DataFrame(validate_scaled, columns=num_train.columns)
    test_scaled = pd.DataFrame(test_scaled, columns=num_train.columns)
    
    
    return train_scaled, validate_scaled, test_scaled

# Combine Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def split_seperate_scale(df, stratify_by= None):
    '''
    This function will take in a dataframe
    seperate the dataframe into train, validate, and test dataframes
    seperate the target variable from train, validate and test
    then it will scale the numeric variables in train, validate, and test
    finally it will return all dataframes individually
    '''
    
    # split data into train, validate, test
    train, validate, test = split(df, stratify_by= None)
    
     # seperate target variable
    X_train, y_train, X_validate, y_validate, X_test, y_test = seperate_y(train, validate, test)
    
    
    # scale numeric variable
    train_scaled, validate_scaled, test_scaled = scale_data(X_train, X_validate, X_test)
    
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test, train_scaled, validate_scaled, test_scaled

# Misc ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def remove_dup_columns(frame):
    keep_names = set()
    keep_icols = list()
    for icol, name in enumerate(frame.columns):
        if name not in keep_names:
            keep_names.add(name)
            keep_icols.append(icol)
    return frame.iloc[:, keep_icols]