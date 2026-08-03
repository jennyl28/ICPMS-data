import streamlit as st

st.title(
    "Mass & Dilution Factors"
)

if "mass_data" not in st.session_state:

    st.warning(
        "Upload Mass File First"
    )

else:

    st.write(
        st.session_state[
            "mass_data"
        ]
    )
