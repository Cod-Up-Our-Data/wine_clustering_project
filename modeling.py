import pandas as pd
import numpy as np
import os
from env import user, pwd, host
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler



####################    ACQUIRE

def acquire_red_df():
    ''' 
     Acquire data from X schema using env imports, rename columns, and storing a cached version of SQL pull as a .csv.
     Specifically, the SQL query returns a df in accordance with SQL script.
     ''' 
    if os.path.exists('winequality-red.csv'):
        print('local version found!')
        return pd.read_csv('winequality-red.csv')
    else:
        df = pd.read_csv('https://query.data.world/s/vca4kc5kqacfufuod2am7poidp5e4a?dws=00000')
        df.to_csv('winequality-red.csv',index=True)
        return df

def acquire_white_df():
    ''' 
     Acquire data from X schema using env imports, rename columns, and storing a cached version of SQL pull as a .csv.
     Specifically, the SQL query returns a df in accordance with SQL script.
     ''' 
    if os.path.exists('winequality-white.csv'):
        print('local version found!')
        return pd.read_csv('winequality-white.csv')
    else:
        df = pd.read_csv('https://query.data.world/s/42ad3ygx65hdnkyo7s4hhpillvmmxm?dws=00000')
        df.to_csv('winequality-white.csv',index=True)
        return df

def merge_wines_df():
    '''
    Takes in two dfs (red/white) and outputs a single merged df for both
    
    '''
    red,white = acquire_red_df(),acquire_white_df()
    red['wine_color'] = 1
    white['wine_color'] = 0
    df = pd.concat([red,white],axis=0,ignore_index=True)
    df.columns = [col.lower().replace(' ','_') for col in df.columns]
    return df


####################    SPLIT


def train_validate_test(df, target):
    '''
    this function takes in a dataframe and splits it into 3 samples, 
    a test, which is 20% of the entire dataframe, 
    a validate, which is 24% of the entire dataframe,
    and a train, which is 56% of the entire dataframe. 
    It then splits each of the 3 samples into a dataframe with independent variables
    and a series with the dependent, or target variable. 
    The function returns 3 dataframes and 3 series:
    X_train (df) & y_train (series), X_validate & y_validate, X_test & y_test. 
    '''
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)

    # split train_validate off into train (70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

        
    # split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    # split validate into X (dataframe, drop target) & y (series, keep target only)
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    # split test into X (dataframe, drop target) & y (series, keep target only)
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test

####################    SCALE


def min_max_scale(X_train, X_validate, X_test, numeric_cols):
    '''
    this function takes in 3 dataframes with the same columns, 
    a list of numeric column names (because the scaler can only work with numeric columns),
    and fits a min-max scaler to the first dataframe and transforms all
    3 dataframes using that scaler. 
    it returns 3 dataframes with the same column names and scaled values. 
    '''
    # create the scaler object and fit it to X_train (i.e. identify min and max)
    # if copy = false, inplace row normalization happens and avoids a copy (if the input is already a numpy array).


    scaler = MinMaxScaler(copy=True).fit(X_train[numeric_cols])

    #scale X_train, X_validate, X_test using the mins and maxes stored in the scaler derived from X_train. 
    # 
    X_train_scaled_array = scaler.transform(X_train[numeric_cols])
    X_validate_scaled_array = scaler.transform(X_validate[numeric_cols])
    X_test_scaled_array = scaler.transform(X_test[numeric_cols])

    # convert arrays to dataframes
    X_train_scaled = pd.DataFrame(X_train_scaled_array, 
                                  columns=numeric_cols).\
                                  set_index([X_train.index.values])

    X_validate_scaled = pd.DataFrame(X_validate_scaled_array, 
                                     columns=numeric_cols).\
                                     set_index([X_validate.index.values])

    X_test_scaled = pd.DataFrame(X_test_scaled_array, 
                                 columns=numeric_cols).\
                                 set_index([X_test.index.values])

    
    return X_train_scaled, X_validate_scaled, X_test_scaled


