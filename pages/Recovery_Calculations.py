import streamlit as st

st.title(
    "Recovery Calculations"
)

if (
    "processed_data"
    not in st.session_state
):

    st.stop()

df = st.session_state[
    "processed_data"
]

recovery_cols = [
    col
    for col
    in df.columns
    if "_mass_corr" in col
]

st.write(
    f"{len(recovery_cols)} "
    "processed isotope channels"
)
