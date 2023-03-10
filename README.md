# **Heritage Housing Issues**
Heritage Housing Issues is a project developed to predict the sale price of houses in the area of Ames, Iowa as requisted by the client.

[Link to deployed app](https://housing-price-data-ml.herokuapp.com/)
---
&nbsp;

## **Table of Content**
- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypothesis and how to validate?](#hypothesis-and-how-to-validate)
- [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [User Stories](#user-stories)
    - [Epic: Data Access](#epic-data-access)
    - [Epic: Model results](#epic-model-results)
    - [Epic: Analysis Details](#epic-analysis-details)
- [Data Preparation](#data-preparation)
    - [Data Cleaning](#data-cleaning)
    - [Feature Engineering](#feature-engineering)
        - [1. Categorical Encoding](#1-categorical-encoding)
        - [2. Numerical Transformations](#2-numerical-transformations)
        - [3. Smart Correlated Selection](#3-smart-correlated-selection)
- [Dashboard Design](#dashboard-design)
    - [Page 1: Quick project summary](#page-1-quick-project-summary)
    - [Page 2: House prices Study of the Ames, Iowa area](#page-2-house-prices-study-of-the-ames-iowa-area)
    - [Page 3: House prices predictor](#page-3-house-prices-predictor)
    - [Page 4: Hypothesises](#page-4-hypothesises)
    - [Page 5: Predict Price](#page-5-predict-price)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Credits](#credits)
- [Content](#content)
---
&nbsp;


## **Dataset Content**
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.


|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|
---
&nbsp;


## **Business Requirements**
As a good friend, you are requested by your friend Lydia Doe, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.
---
&nbsp;


## **Hypothesis and how to validate?**
* 1 - I suspect the Overall condition of the house and overall material and finish of the house will impact the sale price significantly.
    * A Correlation study can help in this investigation.
    * Correct: The correlation study supports this.
* 2 - I suspect the remodel date of the house will be significant in positively impact the price of sale of the house.
    * A Correlation study can help in this investigation.
    * Correct: The correlation study supports this.
* Unexpected results:
    * Houses that are larger in area on various feature are also higher in value. There seems to be a very strong correlation, which was not one of my initial hypothesis.
    * The model will be built around the most important features recognised in the analysis and these will be amongst the most relevant ones.
---
&nbsp;


## **The rationale to map the business requirements to the Data Visualisations and ML tasks**
* Business Requirement 1: Data Visualization and Correlation study
    * I will inspect the data related to the houses in the area of Ames, Iowa.
    * I will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to the house prices.
    * I will plot the variables against the house price to visualise insights.

* Business Requirement 2: Classification, Regression, Cluster and Data Analysis
    * I want to deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses.
    * Use conventional ML to map the relationships between the features and the target.
    * I may consider changing the ML task from Regression to Classification if you find a valid rationale for that.
    * I may conduct extensive hyperparameter optimization for a given algorithm.
---
&nbsp;


## **ML Business Case**
* Business requirements:
    - The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
    - The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.

* Business requirement that can be answered with conventional data analysis:
    - I can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

* Client need:
    - The client needs a dashboard.

* Successful project outcome for the customer will be:
    - A study showing the most relevant variables correlated to sale price.
    - The capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.

* Epics and User Stories:
    - Information gathering and data collection.
    - Data visualization, cleaning, and preparation.
    - Model training, optimization and validation.
    - Dashboard planning, designing, and development.
    - Dashboard deployment and release.

* Ethical or Privacy concerns:
    - There are no Ethical or Privacy concerns. The client found a public dataset.

* Particular model suggested by the data:
    - The data suggests a regressor where the target is the sale price.

* Model's inputs and intended outputs:
     - The inputs are house attribute information and the output is the predicted sale price.

* Criteria for the performance goal of the predictions:
    - Agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.
    - The ML model is considered a failure if after 12 months of usage, the model's predictions are 50% off more than 30% of the time about the offer sale price offer to the customer from potential buyers.

* Benefit for the client:
    - The client will maximize the sales price for the inherited properties.
---
&nbsp;


## **CRISP-DM**
This project uses the CRISP-DM ("CRoss Industry Standard Process for Data Mining") process model to develop the data science process.

| Process | Description |
| --- | --- |
| 1. Business Understanding: | understanding the objectives and requirements |
| 2. Data Understanding | gather data, analyze it and identify opportunities |
| 3. Data Preparation | prepare the data with the appropriate cleaning and engineering for modelling |
| 4. Modelling | research and identify the structure of the model and build it |
| 5. Evaluation | identify the best performing solution and assess if it meets the desired requirements |
| 6. Deployment | move the application into production to allow users to take advantage of it |
---
&nbsp;


## **User Stories**

### ***Epic: Data Access***
- As a **User** I can **access and read** the project summary so that **I can verify the goals / business requirements of the project**.
- As a **User** I can **access and read** the dataset so that **I can assess the data and verify they are relevant to my issue**.
- As a **User** I can **access and analyze** the correlation study and the relative plots so that **I can analyze visually the importance of the various features used to build the model**.

### ***Epic: Model results***
- As a **User** I can **check the results** of the model so that **I can have a prediction of the sale price of my properties**.
- As a **User** I can **input the house details** required by the model so that **I can predict the sale price of another house in the area**.

### ***Epic: Analysis Details***
- As a **User or Data Practitioner** I can **verify the hypotheses** behind the project study so that **I can understand the goals and the results of the data analysis**.
- As a **Data Practitioner** I can **explore the details of the model building process** so that **I can understand and study this process and use it for future development or improvement**.
---
&nbsp;


## **Data Preparation**
Significant amount of data were missing in multiple variables. A further investigation should be held with who collected the data to explore if these variables are actual missing data or refer to the fact that the feature described is actually non present or non relevant. Since this is not possible, further analysis has been performed to individuate if there is any sensible correlation with the missing data values and the others. As an example missing data around the square feet of a second floor might be caused by the fact that the house in question might not have a second floor at all.
&nbsp;

The analysis proceeded as described in the Data Cleaning section.

### ***Data Cleaning***
The variables with missing data are:<br>
    - 2ndFlrSF: 5.9%<br>
    - BedroomAbvGr: 6.8%<br>
    - BsmtFinType1: 7.8%<br>
    - EnclosedPorch: 90.7%<br>
    - GarageFinish: 11.1%<br>
    - GarageYrBlt: 5.5%<br>
    - LotFrontage: 17.7%<br>
    - WoodDeckSF: 89.4%<br>
    - MasVnrArea: 0.55%<br>

The variables 'BedroomAbvGr', 'GarageYrBlt', 'LotFrontage' and 'MasVnrArea' are not normally distributed as shown in the plots. So I decided to replace the missing values with the median instead of the mean.

I decided to handle the features '2ndFlrSF', 'EnclosedPorch' and 'WoodDeckSF' assuming that a missing value would indicate that the feature was 0. I assumed that all three of these features would have 0 square feet indicated because the house had respectively no second floor, nor enclosed porch, nor wood deck. This was to identify in further analysis and data during the house price study if they had any correlation with the target variable, instead of dropping them altogether already at this stage.
For this reason, I've used the ArbitraryNumberImputer to replace the missing values with 0.

I decided the features 'BsmtFinType1' and 'GarageFinish' will be transformed using the CategoricalImputer and replacing the missing values with the most frequently found in the rest of the data for that specific feature.

&nbsp;

### ***Feature Engineering***

#### 1. Categorical Encoding 
Categorical Encoding of object type features to be converted to numerical to suit the regression algorithms.
&nbsp;

#### 2. Numerical Transformations:
| Feature      | Review | Transformation chosen |
| ----------- | ----------- | ----------- |
| 1stFlrSF      | A few transformation improved the distribution, especially log_e | Logarithmic in base e |
| GarageArea   | Yeo Johnson looks like the most effective  | Yeo Johnson |
| GarageYrBlt   | None of the transformations seems to be effective to normalise  | None |
| GrLivArea   | Yeo Johnson looks like the most effective  | Yeo Johnson |
| OverallQual   | None of the transformations seems to be effective to normalise  | None |
| TotalBsmtSF   | Power looks like the most effective once the ouliers are removed  | Power |
| YearBuilt   | None of the transformations seems to be effective to normalise  | None |
| YearRemodAdd   | None of the transformations seems to be effective to normalise  | None |
&nbsp;

#### 3. Smart Correlated Selection:
The result indicates that all features are highly correlated. For obvious reasons we are not going to drop all the variables in the data set, I will move to the modelling phase and evaluate the performance there empirically until the performance is acceptable. If not I will return to this stage for further feature engineering.

---
&nbsp;


## **Dashboard Design**
&nbsp;

### Page 1: Quick project summary
* Quick project summary
	* Describe Project Dataset
	* State Business Requirements

### Page 2: House prices Study of the Ames, Iowa area
* I will list findings related to which features have the strongest correlation to the house sale price.
* Before the analysis, we knew we wanted this page to answer business requirement 1, but we couldn't know in advance which plots would need to be displayed.
* After data analysis, we agreed with stakeholders that the page will: 
	* Have a sample of the data frame containing the data
    * Have visual scatter plots of each variable with a high correlation to the sale price to be able to visually analyze the data.

### Page 3: House prices predictor
* State business requirement 2
* Display the 4 houses' attributes and their respective predicted sale price.
* Display a message informing the summed predicted price for all 4 inherited houses.
* Set of interactive widgets inputs that allow a user to provide real-time house data to predict the sale price. Each set of inputs is related to a given ML task to predict the house sales price.

### Page 4: Hypothesises
* Project hypothesises and how they were validated across the project.

### Page 5: Predict Price
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance
---
&nbsp;


## **Unfixed Bugs**
* None reported at the momement.
---
&nbsp;


## **Deployment**

### Heroku
* The App live link is: https://housing-price-data-ml.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

### [Link to deployed app](https://housing-price-data-ml.herokuapp.com/)
---
&nbsp;


## **Main Data Analysis and Machine Learning Libraries**
* [NumPy](https://numpy.org/) and [Pandas](https://pandas.pydata.org/) which were used to handle the data and data frames essential to the development of this project.
* [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) which were used for data visualization.
* [Feature-engine](https://feature-engine.trainindata.com/en/latest/) which was used for feature engineering and selection.
* [ppscore](https://pypi.org/project/ppscore/) which was used for Predictive Power Score analysis
* [SciPy](https://docs.scipy.org/doc/scipy/reference/stats.html) which was used for feature engineering, specifically its statistical functions.
* [scikit-learn](https://scikit-learn.org/stable/) which was used (GridSearchCV specifically) for hyperparameters research and optimization.
---
&nbsp;


## **Credits** 
The Churnometer walkthrough project - Code Institute learning materials: the majority of the code used was taken from the course material and adapted by me to fit the current project needs.
[Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data) where Code Institute has shared the data set used in this project.
&nbsp;


### ***Content***
#### Documentation Used:
- [ArbitraryNumberImputer in Feature Engine documentation](https://feature-engine.trainindata.com/en/1.0.x/imputation/ArbitraryNumberImputer.html?highlight=ArbitraryNumberImputer)
- [CategoricalImputer in Feature Engine documentation](https://feature-engine.trainindata.com/en/1.0.x/imputation/CategoricalImputer.html)
- [MeanMedianImputer in Feature Engine documentation](https://feature-engine.trainindata.com/en/1.0.x/imputation/MeanMedianImputer.html?highlight=MeanMedianImputer)
- [Markdown guide](https://www.markdownguide.org/)
- [Hyperparameter Optimization tutorial - Youtube](https://www.youtube.com/watch?v=eZ98q7iOUAA)
- [How to use st.write and magic commands](https://www.youtube.com/watch?v=wpDuY9I2fDg)
- [How to Use Streamlit???s st.write Function to Improve Your Streamlit Dashboard](https://towardsdatascience.com/how-to-use-streamlits-st-write-function-to-improve-your-streamlit-dashboard-1586333eb24d)