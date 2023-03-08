import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_ames_data, load_pkl_file
from src.machine_learning.evaluate_performance import model_performance


def page_predict_price_body():

    # load pipeline files
    version = 'v1'
    price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_house_price/{version}/house_price_pipeline.pkl")
    price_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_house_price/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_house_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_house_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_house_price/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_house_price/{version}/y_test.csv")

    st.write("### ML Pipeline: Predict House Prices")
    # display pipeline training summary conclusions
    st.write(
        f"After evaluating different potential algorithms for this model, the choice fell on "
        f"AdaBoostRegressor since the R2 score was excellent and above our initial target of "
        f"0.7 on train and test sets, agreed with the client."
    )
    st.write(
        f"After an extensive hyperparameters research to find the best configuration, the score is: \n"
    )

    st.success(
        f"Train set \n"
        f"R2 Score: 0.827 \n"
    )

    st.success(
        f"Test set \n"
        f"R2 Score: 0.813 \n"
    )
    st.write(
        f"This is an excellent result, exceeding the agreed expectations. "
    )
    st.write("---")

    # show pipeline steps
    st.write(
        "* ML pipeline with feature engineering and best hyperparameters configuration "
        "optimized and refitted with the 3 most important features."
    )
    st.code(price_pipe)
    st.write("---")

    # show best features
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(price_feat_importance)
    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")
    model_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=price_pipe)
