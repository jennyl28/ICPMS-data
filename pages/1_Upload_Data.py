import streamlit as st
import pandas as pd

from icpms_data.data_loader import (
    load_icpms_file
)

from icpms_data.mass_parser import (
    load_mass_file
)

from icpms_data.isotope_detector import (detect_isotope_columns)

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
    df = load_icpms_file(icpms_file)
    st.session_state["raw_data"] = df
    isotope_info = detect_isotope_columns(df)
    st.session_state["isotope_info"] = isotope_info
    
    st.success(
        f"Detected {len(isotope_info)} isotope channels")


if mass_file:

    st.session_state[
        "mass_data"
    ] = load_mass_file(
        mass_file
    )

if has_stds:

    calibration_file = st.file_uploader(
        "Upload Calibration Standards File",
        type=["xlsx"]
    )

    if calibration_file:

        st.session_state[
            "calibration_data"
        ] = pd.read_excel(
            calibration_file
        )
