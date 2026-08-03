import streamlit as st

from icpms_data.blank_corrections import (
    apply_nearest_blank
)

from icpms_data.mass_corrections import (
    apply_mass_correction
)

from icpms_data.dilution_corrections import (
    apply_dilution
)

from icpms_data.calibration_processing import (
    apply_all_calibrations
)

st.title("Process Data")

if "raw_data" not in st.session_state:

    st.warning(
        "Upload ICP-MS file first"
    )

    st.stop()

df = st.session_state[
    "raw_data"
].copy()

isotopes = st.session_state[
    "isotope_info"
]

if st.button("Process Data"):

    for isotope in isotopes:

        cps_col = isotope["column"]

        df = apply_nearest_blank(
            df,
            cps_col
        )

        df = apply_dilution(
            df,
            cps_col
        )

        df = apply_mass_correction(
            df,
            cps_col
        )

    if st.session_state.get(
        "has_standards",
        False
    ):

        (
            df,
            calibration_results
        ) = apply_all_calibrations(
            df,
            isotopes
        )

        st.session_state[
            "calibration_results"
        ] = calibration_results

    st.session_state[
        "processed_data"
    ] = df

    st.dataframe(df)
