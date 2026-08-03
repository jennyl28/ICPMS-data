import streamlit as st

st.set_page_config(page_title="ICPMS Data Analysis", layout="wide")

st.title("ICPMS Data Analysis")
st.write(
    "Upload your ICP-MS data to begin. Once loaded, use the pages "
    "in the sidebar to step through the analysis."
)

st.markdown("""
### Workflow

1. Upload ICP-MS Data
2. Upload Separation Masses
3. Apply Corrections
4. Review QC
5. Export Results

Supports:

-Stable nuclides and radionuclides

Optional calibration standards conversion.
""")
