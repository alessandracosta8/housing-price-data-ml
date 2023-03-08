import streamlit as st
from app_pages.multipage import MultiPage


# Load pages scripts
from app_pages.project_summary import project_summary_body
from app_pages.house_price_study import house_price_study_body

# Create an instance of the app
app = MultiPage(app_name="Predict your house price")

# App pages
app.add_page("Project Summary", project_summary_body)
app.add_page("House price study", house_price_study_body)

# Run the app
app.run()
