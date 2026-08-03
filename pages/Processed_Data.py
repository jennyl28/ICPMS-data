import streamlit as st

from icpms_data.blank_corrections import (
    apply_nearest_blank
)

from icpms_data.dilution_corrections import (
    apply_dilution
)

from icpms_data.mass_corrections import (
    apply_mass_correction
)

st.title("Process Data")

if "raw_data" in st.session_state:

    df = st.session_state[
        "raw_data"
    ].copy()

    isotope = st.text_input(
        "Isotope Column",
        "226 - > 226 Ra"
    )

    if st.button("Process"):

        df = apply_nearest_blank(
            df,
            isotope
        )

        df = apply_dilution(
            df,
            isotope
        )

        df = apply_mass_correction(
            df,
            isotope
        )

        st.session_state[
            "processed_data"
        ] = df

        st.dataframe(df)
