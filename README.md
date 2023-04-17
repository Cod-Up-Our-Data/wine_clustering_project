# wine_clustering_project
#### Welcome to this initial exploration of Wine Quality Data for Red and White wines!  The context of this project is limited to ....
#### The goals of this initial exploration are as follows:
- Create a REGRESSION model which will assign Quality_Score predictions to an unseen set of wines based upon specific drivers such as, alcohol content, volatile_acidity, chlorides, sulfates, etc...
- Utilize clustering models within the exploration phase of the DS pipeline to assist in the discovery of meaningful insights and associations.
- .
- .
- .

#### PROJECT DESCRIPTION:
- As a Minimally Viable Product, 
- 
- 

#### Project Planning:
- Plan: Questions and Hypotheses
- Acquire: Obtain two distinct datasets (red wines/white wines) from https://data.world/food/wine-quality and combine both into a single datset with an attribute which indicates the wine_color.
- Prepare: Kept outliers, missingness was a non-issue, as there were ZERO entries containing NULL values for predictors.  Split into ML subsets (Train/Validate/Test).
- Explore: Univariate and multi-variate analysis, correlation matrix, 2D and 3D visualization, correlation significance testing, 1-sample T-testing, K-Means clustering to discover meaningful sample segments (with associated MinMaxScaling).
- Model: With dataset scaled via MinMaxScaler, Initially, create an MVP model which is a Vanilla Multiple Linear Regression model specifically using ALCOHOL/DENSITY/VOLATILE_ACIDITY.  Experiment with OLS Model hyperparameters
- Deliver: Please refer to this doc as well as the Final_Report.ipynb file for the finished version of the presentation, in addition to a brief 5-min presentation to the DS Team.

#### Initial hypotheses and questions:
#### What meaningful feature sets can be leveraged to create a model that displays the most improved predictive performance when compared to the mean baseline?  What predictor/target correlations exist that would strengthen the predictive power of model X?  What sample means show significant deviation from the overall mean?  Could these sample means indicate features to be used along with correlation information and K-Means Clustering to uncover potential sources of predictive power. 

#### Data Dictionary: 


alcohol:            | float     |   measured as percentage 

volatile_acidity:   | float     |   greater values indicate vinegar-like taste           

sulphates:          | float     |   additive with antimicrobial/antioxidant properties 

citric_acid:        | float     |   a preservative with capacity to add flavor

total_SO2:          | float     |   includes free_SO2

density:            | float     |   an indication of sugar/alcohol content 

chlorides:          | float     |   amount of salts present

fixed_acidity:      | float     |   non-volatile acids not subject to evaporation

ph:                 | float     |   acidity-base measurement

free_SO2:           | float     |   antimicrobial/antioxidant properties 

residual_sugar:     | float     |   measured to indicate sweetness 

wine_color:         | int       |   1-Red / 0-White

quality:            | int       |   TARGET: rating given by a wine-tasting professional 

#### Instructions for those who wish to reproduce this work or simply follow along:
You Will Need (ALL files must be placed in THE SAME FOLDER!):
- 1. final_report.ipynb file from this git repo
- 2. wrangle.py file from this git repo
- 3. XXX.py file from this git repo
- 4. XXX.py file from this git repo
- 5. env.py file to be generated by IT.  You must use your own env.py file with your own sign-in credentials.  Please contact IT if you are in need of obtaining this.  Otherwise, feel free to create your env.py script with any text editor by following these steps:

- In your newly opened file, we will place 2 Blocks of Info.  Copy/Paste the following three lines:

            host = 'address for database server'
            user = 'your assigned user name'
            pwd = 'the password associated with your user name'

            # The 2nd Block of Info: (Copy/Paste the 2nd Block below the 1st Block)
            def get_db_url(db_name,u_name=user,pwd=pwd,h_name=host):
                return f'mysql+pymysql://{u_name}:{pwd}@{h_name}/{db_name}'

Ensure:
- All X files are in the SAME FOLDER
- wrangle.py and env.py each have the .py extension in the file name
- The two Blocks of Info in the env.py file are all aligned at the left-most index of the page EXCEPT the final line of code beginning with "return".  This line should be 4 whitespaces (or 1 TAB) indented from the rest.
- If your choose to CREATE your env.py file, ensure that each of the 3 string values (host,uname,pwd) are wrapped in single-quotes ' ' as in the example.

Any further assistance required, please email me at myemail@somecompany.com.


#### Findings, Recommendations, and Takeaways:

- 