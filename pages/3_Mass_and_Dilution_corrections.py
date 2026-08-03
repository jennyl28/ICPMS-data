import streamlit as st
import pandas as pd

st.title(
    "Mass & Dilution Corrections"
)

if "isotope_info" in st.session_state:

    st.subheader(
        "Detected Isotopes"
    )

    isotope_df = pd.DataFrame(
        st.session_state[
            "isotope_info"
        ]
    )

    st.dataframe(
        isotope_df,
        use_container_width=True
    )
