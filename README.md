## Dataset Content
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





## Business Requirements
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.


## Hypothesis and how to validate?
* 1 - I suspect the Overall condition of the house and overall material and finish of the house will impact the sale price significantly.
    * A Correlation study can help in this investigation.
* 2 - I suspect the remodel date of the house will be significant in positively impact the price of sale of the house.
    * A Correlation study can help in this investigation.



## The rationale to map the business requirements to the Data Visualisations and ML tasks
* Business Requirement 1: Data Visualization and Correlation study
    * I will inspect the data related to the houses in the area of Ames, Iowa.
    * I will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to the house prices.
    * I will plot the variables against the house price to visualise insights.

* Business Requirement 2: Classification, Regression, Cluster and Data Analysis
    * I want to deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses.
    * Use conventional ML to map the relationships between the features and the target.
    * I may consider changing the ML task from Regression to Classification if you find a valid rationale for that.
    * I may conduct extensive hyperparameter optimization for a given algorithm.


## ML Business Case
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



## Dashboard Design

### Page 1: Quick project summary
* Quick project summary
	* Describe Project Dataset
	* State Business Requirements

### Page 2: House prices Study of the Ames, Iowa area
* I will list findings related to which features have the strongest correlation to the house sale price.
* Before the analysis, we knew we wanted this page to answer business requirement 1, but we couldn't know in advance which plots would need to be displayed.
* After data analysis, we agreed with stakeholders that the page will: 
	* State business requirement 1

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


## Unfixed Bugs
* None reported at the momement.
<!--- You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed. --->

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Link to deployed app
[Churnometer live app](https://churnometer-ml-project.herokuapp.com/)

## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.

