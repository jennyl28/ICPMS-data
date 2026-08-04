import streamlit as st
import pandas as pd

from icpms_data.data_loader import load_icpms_file
from icpms_data.mass_parser import load_mass_file
from icpms_data.isotope_detector import detect_isotope_columns

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

st.session_state["has_cal_standards"] = has_stds

if icpms_file:

    try:

        df = load_icpms_file(
            icpms_file
        )

        st.session_state["raw_data"] = df

        isotope_info = detect_isotope_columns(
            df
        )

        st.session_state[
            "isotope_info"
        ] = isotope_info

        st.success(
            f"Detected {len(isotope_info)} isotope channels"
        )

        # Temporary debugging
        st.write("Columns:")
        st.write(df.columns.tolist())

        st.write("Preview:")
        st.dataframe(df.head())

    except Exception as e:

        st.error(
            f"Error loading ICP-MS file: {e}"
        )

if mass_file:

    try:

        mass_data = load_mass_file(
            mass_file
        )

        st.session_state[
            "mass_data"
        ] = mass_data

        st.success(
            "Mass file loaded successfully"
        )

    except Exception as e:

        st.error(
            f"Error loading mass file: {e}"
        )

if has_stds:

    st.info(
        "Calibration standards will be extracted from the ICP-MS file."
    )
