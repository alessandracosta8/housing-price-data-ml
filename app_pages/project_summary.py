import streamlit as st


def project_summary_body():

    st.header("Project Summary")

    st.write(
        """
        I was trusted by the client to perform a study of the house prices in Ames, Iowa. \n
        This project has the goal to examinate the house prices in the area and build a 
        Machine learning model to predict the potential price. \n
        """
    )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        """
        * For additional information, please visit and **read** the 
        [Project README file](https://github.com/alessandracosta8/housing-price-data-ml).
        """
    )

    # copied from README file - "Business Requirements" section
    st.subheader(
        "Business requirements:"
    )

    st.write(
        "The project has 2 business requirements:\n"
    )

    st.success(
        """
        1 - The client is interested in discovering how the house attributes correlate with 
        the sale price. Therefore, the client expects data visualisations of the correlated 
        variables against the sale price to show that. \n
        """
    )

    st.success(
        """
        2 - The client is interested in predicting the house sale price from her four 
        inherited houses and any other house in Ames, Iowa.\n\n
        """
    )
