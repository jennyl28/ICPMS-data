import streamlit as st
import pandas as pd

st.title(
    "Mass & Dilution Corrections"
)

st.write(
    "Session State Keys:"
)

st.write(
    list(st.session_state.keys())
)

if "isotope_info" not in st.session_state:

    st.warning(
        "No isotope information found. Please upload an ICP-MS file first."
    )

    st.stop()

isotope_info = st.session_state[
    "isotope_info"
]

st.write(
    f"Number of isotopes detected: {len(isotope_info)}"
)

st.dataframe(
    pd.DataFrame(isotope_info),
    use_container_width=True
)
