import streamlit as st
from app_pages.multipage import MultiPage


# Load pages scripts
from app_pages.project_summary import project_summary_body
from app_pages.house_price_study import house_price_study_body
from app_pages.predict_price import predict_house_prices_body
from app_pages.project_hypothesis import page_project_hypothesis_body
from app_pages.pipeline_details import page_predict_price_body

# Create an instance of the app
app = MultiPage(app_name="Predict your house price")

# App pages
app.add_page("Project Summary", project_summary_body)
app.add_page("House Price Study", house_price_study_body)
app.add_page("Predict House Prices", predict_house_prices_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Predicting price", page_predict_price_body)

# Run the app
app.run()
