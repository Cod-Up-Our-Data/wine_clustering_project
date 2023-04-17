# wine_clustering_project
#### Welcome to this initial exploration of Wine Quality Data for Red and White wines!  The context of this project is limited to ....
#### The goals of this initial exploration are as follows:
- Create a REGRESSION model which will assign Quality_Score predictions to an unseen set of wines based upon specific drivers such as, alcohol content, volatile_acidity, chlorides, sulfates, etc...
- Utilize clustering models within the exploration phase of the DS pipeline to assist in the discovery of meaningful insights and associations.
- .
- .
- .

#### PROJECT DESCRIPTION:
- 
- 
- 

#### Project Planning:
- Plan: Questions and Hypotheses
- Acquire: Obtain two distinct datasets (red wines/white wines) from https://data.world/food/wine-quality and combine both into a single datset with an attribute which indicates the wine_color.
- Prepare: Kept outliers, missingness was a non-issue, as there were ZERO entries containing NULL values for predictors.  Split into ML subsets (Train/Validate/Test).
- Explore: Univariate and multi-variate analysis, correlation matrix, 2D and 3D visualization, correlation significance testing, 1-sample T-testing, K-Means clustering to discover meaningful sample segments.
- Model: Initially, create an MVP model which is a Vanilla Multiple Linear Regression model specifically using ALCOHOL/DENSITY/VOLATILE_ACIDITY.  Given the short-fused nature of the project, large, non-refined steps will be taken to find meaningful recommendations.  For example, a transition from a Multiple Linear Model to a Random Forest Regressor may not be accompanied by the expected tuning of important hyper-parameters for the new model.  We are looking to obtain a Vanilla-to-Vanilla comparison of the various models, while also knowing that significantly different results will come with further tuning.
- Deliver: Please refer to this doc as well as the Final_Report.ipynb file for the finished version of the presentation, in addition to a brief 5-min presentation to the DS Team.

#### Initial hypotheses and questions:
#### What meaningful feature sets can be leveraged to create a model that displays the most improved predictive performance when compared to the mean baseline?  What predictor/target correlations exist that would strengthen the predictive power of model X?  What sample means show significant deviation from the overall mean?  Could these sample means indicate features to be used along with correlation information and K-Means Clustering to uncover potential sources of predictive power. 

#### Data Dictionary: 


alcohol:           | float    |   measured as percentage 

volatile_acidity:          | float      |   greater values indicate vinegar-like taste           

sulphates:           | float      |   additive with antimicrobial/antioxidant properties 

citric_acid:  | float      |   a preservative with capacity to add flavor

total_SO$_{2}$:          | float      |   includes free_SO$_{2}$

lotsqft:        | float      |   square footage of land subject to tax calculations 

fips:           | object     |   Federal county code: 6037 LA County, 6059 Orange County, 6111 Ventura County (California)

city:           | object     |   Propietary Code used to denote City, mapping is currently unavailable

o_sqft:         | float      |   an attempt to combine SQFT-BEDS-BATHS into one data point to reduce effects of colinearity