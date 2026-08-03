import streamlit as st

from icpms_data.exports import (
    export_excel
)

st.title("Export")

if (
    "processed_data"
    in st.session_state
):

    excel_data = export_excel(
        st.session_state[
            "processed_data"
        ]
    )

    st.download_button(
        "Download Results",
        excel_data,
        "Processed_Results.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
