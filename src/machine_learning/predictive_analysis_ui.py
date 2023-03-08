import streamlit as st


def predict_price(X_live, price_features, price_pipeline):

    # from live data, subset features related to this pipeline
    X_live_price = X_live.filter(price_features)

    # predict
    house_price = price_pipeline.predict(X_live_price)
    price_predicted = int(house_price)

    return price_predicted
