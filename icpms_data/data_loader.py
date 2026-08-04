import pandas as pd

def load_icpms_file(uploaded_file):

    raw = pd.read_excel(
        uploaded_file,
        header=None
    )

    raw = raw.set_index(0)

    df = raw.T

    df = df.reset_index(
        drop=True
    )

    return df
