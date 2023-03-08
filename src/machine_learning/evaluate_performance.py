import streamlit as st
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


def model_performance(X_train, y_train, X_test, y_test, pipeline):

    st.write("### Train Set")
    pipeline_results(X_train, y_train, pipeline)

    st.write("### Test Set")
    pipeline_results(X_test, y_test, pipeline)


def pipeline_results(X, y, pipeline):
    prediction = pipeline.predict(X)
    st.write('R2 Score:', r2_score(y, prediction).round(3))
    st.write('Mean Squared Error:', mean_squared_error(y, prediction).round(3))
    st.write('Mean Absolute Error:',
             mean_absolute_error(y, prediction).round(3))
