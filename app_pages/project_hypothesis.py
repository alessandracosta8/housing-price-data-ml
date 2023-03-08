import streamlit as st


def page_project_hypothesis_body():

    st.header("Project Hypothesis and Validation")

    st.subheader("First Hypothesis:")
    st.write(
        f"I suspected the Overall condition of the house and overall material and finish of the house "
        f"will impact the sale price significantly."
    )
    st.success(
        f"Correct: \n"
        f"The correlation study supports this."
    )

    st.subheader("Second Hypothesis:")
    st.write(
        f"I suspected the remodel date of the house will be significant in positively impact the price "
        f"of sale of the house."
    )
    st.success(
        f"Correct: \n"
        f"The correlation study supports this."
    )

    st.subheader("Unexpected results:")
    st.info(
        f"Houses that are larger in area on various feature are also higher in value. This seems to be "
        f"the strongest correlation, which was not one of my initial hypothesis."
    )
