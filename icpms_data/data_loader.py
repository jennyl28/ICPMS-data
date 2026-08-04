import pandas as pd


def load_icpms_file(uploaded_file):

    # Read raw workbook
    raw = pd.read_excel(
        uploaded_file,
        sheet_name=0,
        header=None
    )

    df = raw.T

    return df
