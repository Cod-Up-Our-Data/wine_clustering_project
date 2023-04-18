import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.color_palette("tab10")
from scipy import stats
from sklearn.model_selection import train_test_split
import os
seed = 1349

############### Acquire
def acquire():
    '''
    Obtains the vanilla version of both the red and white wine dataframe
    INPUT:
    NONE
    OUTPUT:
    red = pandas dataframe with red wine data
    white = pandas dataframe with white wine data
    '''
    red = pd.read_csv('https://query.data.world/s/k6viyg23e4usmgc2joiodhf2pvcvao?dws=00000')
    white = pd.read_csv('https://query.data.world/s/d5jg7efmkn3kq7cmrvvfkx2ww7epq7?dws=00000')
    return red, white

def prepare_mvp():
    '''
    Takes in the vanilla red and white wine dataframes and returns a cleaned version that is ready 
    for exploration and further analysis
    INPUT:
    NONE
    OUTPUT:
    wines = pandas dataframe with both red and white wine prepped for exploration
    '''
    red, white = acquire()
    red['is_red'] = 1
    white['is_red'] = 0
    wines = pd.concat([red, white], ignore_index = True)
    return wines

def wrangle():
    '''
    Function that acquires, prepares, and splits the wines dataframe for use as well as 
    creating a csv.
    INPUT:
    NONE
    OUTPUT:
    .csv = ONLY IF FILE NONEXISTANT
    wines = pandas dataframe with both red and white wine prepped for exploration
    '''
    if os.path.exists('wines.csv'):
        wines = pd.read_csv('wines.csv', index_col=0)
        train, validate, test = split_wines(wines)
        return train, validate, test
    else:
        red, white = acquire()
        wines = pd.concat([red, white], ignore_index = True)
        wines.to_csv('wines.csv')
        train, validate, test = split_wines(wines)
        return train, validate, test



def split_wines(df):
    '''
    This function takes in a dataframe and splits it into 3 data sets
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    #split_db class verision with random seed
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed)
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed)
    return train, validate, test


def coorelation():
    
    cols = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol', 'quality', 'is_red']
    
    
    
    for col in cols:
        sns.regplot(data=train, x=col, y='quality', line_kws={'color':'red'})
        plt.title(f'{col} vs quality')
        plt.show()
        r, p = stats.spearmanr(train[col], train.quality)
        alpha = 0.05
        if p < alpha:
            print(f'\033[32mREJECT NULL HYPOTHESIS!\033[0m')
            print(f'\033[35mFeature:\033[0m {col}')
            print(f'\033[35mCorrelation:\033[0m {r:.4f}')
            print(f'\033[35mP-Value:\033[0m {p:.4f}')
        else:
            print(f'\033[31mACCEPT NULL HYPOTHESIS!\033[0m')
            print(f'\033[35mFeature:\033[0m {col}')
            print(f'\033[35mCorrelation:\033[0m {r:.4f}')
            print(f'\033[35mP-Value:\033[0m {p:.4f}')
        
train, validate, test = wrangle()


def full_split_wines(train, validate, test, target):
    '''
    accepts train, validate, test data sets and the name of the target variable as a parameter
    splits the data frame into:
    X_train, X_validate, X_test, y_train, y_validate, y_test
    '''
    #train, validate, test = train_validate_test_split(df, target)

    #save target column
    y_train = train[target]
    y_validate = validate[target]
    y_test = test[target]

    #remove target column from the sets
    train.drop(columns = target, inplace=True)
    validate.drop(columns = target, inplace=True)
    test.drop(columns = target, inplace=True)

    return train, validate, test, y_train, y_validate, y_test