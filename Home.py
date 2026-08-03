import streamlit as st

from aqam_da.loader import load_spreadsheet

st.set_page_config(page_title="ICPMS Data Analysis", layout="wide")

st.title("ICPMS Data Analysis")
st.write(
    "Upload your ICP-MS data to begin. Once loaded, use the pages "
    "in the sidebar to step through the analysis."
)

# Entry point for the whole app - everything downstream reads from
# st.session_state, which is how pages pass data to each other in Streamlit.
analyst_name = st.text_input("Analyst name")
uploaded_file = st.file_uploader("ICP-MS run spreadsheet", type=["xlsx", "xls"])

if uploaded_file is not None:
    df, element_labels = load_spreadsheet(uploaded_file)
    st.session_state["raw_data"] = df
    st.session_state["element_labels"] = element_labels
    st.session_state["analyst_name"] = analyst_name
    st.session_state["source_filename"] = uploaded_file.name
    st.success(f"Loaded {uploaded_file.name} — {df.shape[0]} rows, {df.shape[1]} columns.")

if "raw_data" in st.session_state:
    # Reminds you what's currently loaded even after navigating away and back.
    st.caption(f"Currently loaded: {st.session_state['source_filename']}")
