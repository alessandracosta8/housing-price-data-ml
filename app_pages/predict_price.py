import streamlit as st
import pandas as pd
from src.data_management import load_ames_data, load_pkl_file, load_inherited_houses_data
from src.machine_learning.predictive_analysis_ui import predict_price


def predict_house_prices_body():

    # load pipeline files
    version = 'v1'
    price_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_house_price/{version}/house_price_pipeline.pkl")

    price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_house_price/{version}/X_train.csv")
                      .columns
                      .to_list()
                      )

    st.header("Predict house sale price of homes in Ames, Iowa.")

    st.subheader("Business Requirement 2:")
    st.write(
        f"The client is interested in predicting the house sale price "
        f"from her four inherited houses and any other house in Ames, Iowa."
    )
    st.write(
        f"Based on this request this application will predict the price for the four houses "
        f"belonging to the client and give the ability to calculate the price of any "
        f"house in the area of Ames, Iowa as long as the user is in possessions of the data "
        f"reguarding the 3 features need for the model to predict. \n"
        f"These being: \n "
        f"* OverallQual - Rates the overall material and finish of the house \n "
        f"* GrLivArea - Above grade (ground) living area square feet \n "
        f"* TotalBsmtSF - Total square feet of basement area"
    )

    st.write("---")

    # Price prediction for the client houses
    st.subheader("Predicted sale price for the clients properties.")

    # load client's houses data
    client_houses = load_inherited_houses_data()

    # display data from client's houses
    if st.checkbox("Click to display the Client's houses details"):
        st.write(
            f"The data set has {client_houses.shape[0]} rows and {client_houses.shape[1]} columns. \n"
            f"The details about each feature of the houses are displayed in this data frame."
        )

        st.write(client_houses.head(4))
    
    property_1 = predict_price(client_houses.iloc[[0]], price_features, price_pipeline)
    property_2 = predict_price(client_houses.iloc[[1]], price_features, price_pipeline)
    property_3 = predict_price(client_houses.iloc[[2]], price_features, price_pipeline)
    property_4 = predict_price(client_houses.iloc[[3]], price_features, price_pipeline)

    st.write(f"Client's property 1 has a predicted house price of **${property_1}**.")
    st.write(f"Client's property 2 has a predicted house price of **${property_2}**.")
    st.write(f"Client's property 3 has a predicted house price of **${property_3}**.")
    st.write(f"Client's property 4 has a predicted house price of **${property_4}**.")


    st.write("---")

    # Widget to predict any potential house in the area
    st.subheader("Enter the house details to predict the price:")

    # Generate live data
    X_live = DrawInputsWidgets()

    live_price_prediction = predict_price(
        X_live, price_features, price_pipeline)

    # predict on live data
    if st.button('Predict House Sale Price'):
        price_prediction = predict_price(
            X_live, house_features, pipeline_model
        )

        st.write(
            f"The Predicted Sale Price for this house is: ** $ {live_price_prediction} ** "
        )

    st.write("---")


def DrawInputsWidgets():

    # load dataset
    df = load_ames_data()
    percentageMin, percentageMax = 0.4, 2.0

    # we create input widgets only for 3 features
    col1, col2, col3 = st.beta_columns(3)

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "OverallQual"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col3:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    return X_live
