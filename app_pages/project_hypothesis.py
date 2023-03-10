import streamlit as st


def page_project_hypothesis_body():

    st.header("Project Hypothesis and Validation")

    st.subheader("First Hypothesis:")
    st.write(
        """
        I suspected the Overall condition of the house and overall material and finish of the house 
        will impact the sale price significantly.
        """
    )
    st.success(
        """
        Correct: \n
        The correlation study supports this.
        """
    )

    st.subheader("Second Hypothesis:")
    st.write(
        """
        I suspected the remodel date of the house will be significant in positively impact the price 
        of sale of the house.
        """
    )
    st.success(
        """
        Correct: \n
        The correlation study supports this.
        """
    )

    st.subheader("Unexpected results:")
    st.info(
        """
        Houses that are larger in area on various feature are also higher in value. There seems to be 
        a very stong correlation, which was not one of my initial hypothesis.
        """
    )
