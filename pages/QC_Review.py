import streamlit as st
import pandas as pd

st.title("QC Review")

if (
    "calibration_results"
    in st.session_state
):

    qc = []

    for (
        isotope,
        fit
    ) in st.session_state[
        "calibration_results"
    ].items():

        qc.append({
            "Isotope": isotope,
            "Slope": fit["slope"],
            "Intercept": fit[
                "intercept"
            ],
            "R²": fit["r2"]
        })

    st.dataframe(
        pd.DataFrame(qc),
        use_container_width=True
    )
