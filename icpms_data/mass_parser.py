import pandas as pd


def load_mass_file(uploaded_file):

    df = pd.read_csv(
        uploaded_file
    )

    df.columns = [
        str(col).strip()
        for col in df.columns
    ]

    return df
