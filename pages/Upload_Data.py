import streamlit as st

from icpms_data.data_loader import (
    load_icpms_file
)

from icpms_data.mass_parser import (
    load_mass_file
)


st.title("Upload Data")

icpms_file = st.file_uploader(
    "ICP-MS File",
    type=["xlsx"]
)

mass_file = st.file_uploader(
    "Mass File",
    type=["xlsx"]
)

has_stds = st.checkbox(
    "Calibration Standards Included"
)

st.session_state[
    "has_cal_standards"
] = has_stds

if icpms_file:

    st.session_state[
        "raw_data"
    ] = load_icpms_file(
        icpms_file
    )

if mass_file:

    st.session_state[
        "mass_data"
    ] = load_mass_file(
        mass_file
    )
