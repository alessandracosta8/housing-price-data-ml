import plotly.express as px
import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_ames_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def house_price_study_body():

    # load data
    df = load_ames_data()

    # correlated study results -> features with high correlation
    vars_to_study = [
        '1stFlrSF',
        'GarageArea',
        'GarageYrBlt',
        'GrLivArea',
        'KitchenQual_Ex',
        'KitchenQual_TA',
        'OverallQual',
        'TotalBsmtSF',
        'YearBuilt',
        'YearRemodAdd'
    ]

    st.header("House price study")
    st.write(
        """
        The client is interested in discovering how house attributes correlate with sale prices. 
        Therefore, the client expects data visualizations of the correlated variables against 
        the sale price.
        """
    )

    # inspect data
    if st.checkbox("Inspect house data from the area"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        """
        * A correlation study was conducted in the notebook to better understand how 
        the variables are correlated to the houses sale price. \n
        The most correlated variable are: \n
        """
        f"**{vars_to_study}**"
    )

    st.info(
        """
        The correlation indications and plots below interpretation converge. \n
        It is indicated that: \n
        * Houses that are **larger in area** on various feature are also higher in value. 
        This seemed to be the strongest correlation in the initial part of the analysis, 
        which was not one of the initial hypothesis. Further assessment has still confirmed 
        overall quality as the most important feature, in a later stage when evaluating the model
        and assessing feature importance. \n
        * Houses that are in **better condition** and with **higher quality** building features are higher in value, 
        confirming hypothesis 1. \n
        * Houses which are **newer or more recently renovated** are higher in value, confirming hypothesis 2. \n
        """
    )

    # load data frame
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # function to display plots of the variables to study
    def scatter_plot_for_eda(df, col, target_var):
        fig = plt.figure(figsize=(12, 6))
        sns.scatterplot(data=df, x=col, y=target_var)
        plt.title(f"{col}", fontsize=20, y=1.05)
        st.pyplot(fig)

    def plot_categorical(df, col, target_var):
        fig, axes = plt.subplots(figsize=(12, 5))
        sns.countplot(data=df, x=col, hue=target_var,
                      order=df[col].value_counts().index)
        plt.xticks(rotation=90)
        plt.title(f"{col}", fontsize=20, y=1.05)
        st.pyplot(fig)

    def variables_plots(df_eda):
        target_var = 'SalePrice'

        for col in df_eda.drop([target_var], axis=1).columns.to_list():
            if df_eda[col].dtype == 'object':
                plot_categorical(df_eda, col, target_var)
            else:
                scatter_plot_for_eda(df_eda, col, target_var)

    # Individual plots per variable
    if st.checkbox("Variables Plots - visual analysis"):
        variables_plots(df_eda)
