import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Export Results")

if (
    "processed_data"
    not in st.session_state
):

    st.stop()

df = st.session_state[
    "processed_data"
]

buffer = BytesIO()

with pd.ExcelWriter(
    buffer,
    engine="xlsxwriter"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Results",
        index=False
    )

    if (
        "calibration_results"
        in st.session_state
    ):

        pd.DataFrame(
            st.session_state[
                "calibration_results"
            ]
        ).T.to_excel(
            writer,
            sheet_name="Calibration_QC"
        )

st.download_button(
    "Download Results",
    buffer.getvalue(),
    "ICPMS_Results.xlsx",
    mime=(
        "application/vnd.openxmlformats-"
        "officedocument.spreadsheetml.sheet"
    )
)
