# wine_clustering_project
#### Welcome to this initial exploration of Wine Quality Data for Red and White wines!  The context of this project is derived from the combination of two datasets which contain technical measurements and quality scores for wines in Northern Portugal.
#### The goals of this initial exploration are as follows:
- Create a REGRESSION model which will assign Quality_Score predictions to an unseen set of wines based upon specific drivers such as, alcohol content, volatile_acidity, chlorides, sulfates, etc...
- Utilize clustering models within the exploration phase of the DS pipeline to assist in the discovery of meaningful insights and associations.
- Model predictions wil be utilized by the California Wine Institute to better inform Marketing, R&D, and Supply Chain decisions taken by the Institute.

#### PROJECT DESCRIPTION:
- As a Minimally Viable Product, we intend to create a workable REGRESSION model, designed to provide useable information at a low-level of granularity. 
- As the model becomes more refined, the level of granularity will become more sensitive to the dataset.
- Exploration of the dataset using Clustering presents an opportunity to gain insights which could not be garnered otherwise.

#### Project Planning:
- Plan: Questions and Hypotheses
- Acquire: Obtain two distinct datasets (red wines/white wines) from https://data.world/food/wine-quality and combine both into a single datset with an attribute which indicates the wine_color.
- Prepare: Kept outliers, missingness was a non-issue, as there were ZERO entries containing NULL values for predictors.  Split into ML subsets (Train/Validate/Test).
- Explore: Univariate and multi-variate analysis, correlation matrix, 2D and 3D visualization, correlation significance testing, 1-sample T-testing, K-Means clustering to discover meaningful sample segments (with associated MinMaxScaling).
- Model: With dataset scaled via MinMaxScaler, Initially, create an MVP model which is a Vanilla Multiple Linear Regression model specifically using ALCOHOL/DENSITY/VOLATILE_ACIDITY.  Experiment with OLS Model hyperparameters
- Deliver: Please refer to this doc as well as the Final_Report.ipynb file for the finished version of the presentation, in addition to a brief 5-min presentation to the DS Team.

#### Initial hypotheses and questions:
* What meaningful feature sets can be leveraged to create a model that displays the most improved predictive performance when compared to the mean baseline?  

* What predictor/target correlations exist that would strengthen the predictive power of model X?  

* What sample means show significant deviation from the overall mean? 

* Could these sample means indicate features to be used along with correlation information and K-Means Clustering to uncover potential sources of predictive power. 

#### Data Dictionary: 


|Feature |  Data type | Definition |
|---|---|---|
| alcohol: | float | measured as percentage |
| volatile_acidity: | float | greater values indicate vinegar-like taste |
| sulphates: | float | additive with antimicrobial/antioxidant properties |
| citric_acid: | float | a preservative with capacity to add flavor |
| total_SO2: | float | includes free_SO2 |
| density: | float | an indication of sugar/alcohol content |
| chlorides: | float | amount of salts present |
| fixed_acidity: | float | non-volatile acids not subject to evaporation |
| ph: | float | acidity-base measurement |
| free_SO2: | float | antimicrobial/antioxidant properties |
| residual_sugar: | float | measured to indicate sweetness |
| wine_color: | int | 1-Red / 0-White |
| quality: | int | TARGET: rating given by a wine-tasting professional |

#### Instructions for those who wish to reproduce this work or simply follow along:
You Will Need (ALL files must be placed in THE SAME FOLDER!):
- 1. final_wine_project.ipynb file from this git repo
- 2. final_wrangle.py file from this git repo
- 3. final_modeling.py file from this git repo

Ensure:
- All files are in the SAME FOLDER
- final_wrangle.py and final_modeling.py each have the .py extension in the file name

Any further assistance required, please email me at myemail@somecompany.com.


#### Findings, Recommendations, and Takeaways:

- Modeling results may improve by subsetting the dataset on wine_color.
- Outliers do need to be dealt with.  Rather than setting a blanket rule for all features, a column-by-column appraoch to defining and removing outliers may prove beneficial for modeling.
- Getting more non-technical data may prove beneficial.  How certain can we be that each Quality Score is a function of an objective process?  Does the possibility for subjective factors exist at such a magnitude that it may create noisy data?
- Potential dimensionality reduction (PCA/ t-SNE) may assist with cluster identification.
- Continue to tune model hyperparameters
