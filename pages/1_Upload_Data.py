import streamlit as st
import pandas as pd

from icpms_data.data_loader import load_icpms_file
from icpms_data.mass_parser import load_mass_file
from icpms_data.isotope_detector import detect_isotope_columns

st.title("Upload Data")

# ----------------------------
# File Uploads
# ----------------------------

icpms_file = st.file_uploader(
    "ICP-MS File",
    type=["csv"]
)

mass_file = st.file_uploader(
    "Mass File",
    type=["csv"]
)

# ----------------------------
# Calibration Standards
# ----------------------------

has_stds = st.checkbox(
    "Calibration Standards Included"
)

st.session_state["has_cal_standards"] = has_stds

# ----------------------------
# ICP-MS Data
# ----------------------------

if icpms_file:

    try:

        df = load_icpms_file(
            icpms_file
        )

        st.session_state[
            "raw_data"
        ] = df

        isotope_info = (
            detect_isotope_columns(df)
        )

        st.session_state[
            "isotope_info"
        ] = isotope_info

        st.success(
            f"Loaded {len(df)} samples"
        )

        st.success(
            f"Detected {len(isotope_info)} isotopes"
        )

        st.write(
            f"Data Shape: {df.shape}"
        )

        # Optional automatic standard detection
        if "Type" in df.columns:

            detected_stds = (
                df["Type"]
                .astype(str)
                .str.contains(
                    "CalStd",
                    case=False,
                    na=False
                )
                .any()
            )

            if detected_stds:

                st.info(
                    "Calibration standards detected in uploaded file."
                )

        with st.expander(
            "Preview ICP-MS Data"
        ):

            st.dataframe(
                df,
                width="stretch"
            )

        with st.expander(
            "Detected Columns"
        ):

            st.write(
                df.columns.tolist()
            )

        with st.expander(
            "Detected Isotopes"
        ):

            isotope_df = pd.DataFrame(
                isotope_info
            )

            st.dataframe(
                isotope_df,
                width="stretch"
            )

    except Exception as e:

        st.error(
            f"Error loading ICP-MS file: {e}"
        )

# ----------------------------
# Mass File
# ----------------------------

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

        with st.expander(
            "Preview Mass Data"
        ):

            st.dataframe(
                mass_data,
                width="stretch"
            )

    except Exception as e:

        st.error(
            f"Error loading mass file: {e}"
        )

# ----------------------------
# Standards Status
# ----------------------------

if has_stds:

    st.info(
        "Calibration standards will be extracted from the ICP-MS file."
    )
