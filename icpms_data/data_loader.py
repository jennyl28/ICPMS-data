import pandas as pd

def load_icpms_file(uploaded_file):

    raw = pd.read_excel(
        uploaded_file,
        sheet_name=0,
        header=None
    )

    raw = raw.T

    raw.columns = raw.iloc[0]

    raw = raw.iloc[1:].reset_index(
        drop=True
    )
    st.write("Shape")
    st.write(df.shape)
    
    st.write("Top left corner")
    
    st.dataframe(
        df.iloc[:20, :20])

    return raw
