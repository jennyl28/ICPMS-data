import pandas as pd

def load_icpms_file(uploaded_file):

    df = pd.read_excel(
        uploaded_file,
        sheet_name=0,
        header=None
    )

    return df
