import streamlit as st


def project_summary_body():

    st.write("### Project Summary")

    st.info(
        f"I was trusted by the client to perform a study of the house prices in Ames, Iowa."
        f"This project has the goal to examinate the house prices in the area and build a "
        f"Machine learning model to predict the potential house price of any house of the area."
    )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/alessandracosta8/housing-price-data-ml).")
    
    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"1 - The client is interested in discovering how the house attributes correlate with " 
        f"the sale price. Therefore, the client expects data visualisations of the correlated "
        f"variables against the sale price to show that."
        f"2 - The client is interested in predicting the house sale price from her four "
        f"inherited houses and any other house in Ames, Iowa."
        )
