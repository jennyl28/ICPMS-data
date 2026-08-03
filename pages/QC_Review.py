import streamlit as st

from icpms_data.utils import (
    build_qc_table
)

st.title("QC Review")

if "processed_data" in st.session_state:

    qc = build_qc_table(
        st.session_state[
            "processed_data"
        ]
    )

    st.session_state[
        "qc_table"
    ] = qc

    st.dataframe(
        qc,
        use_container_width=True
    )
