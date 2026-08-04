import pandas as pd


def load_icpms_file(uploaded_file):

    raw = pd.read_excel(
        uploaded_file,
        header=None
    )

    # File is parameter rows x sample columns
    raw = raw.T

    # First row after transpose contains labels
    first_col = raw.iloc[:, 0]

    # Use first column as row index
    raw.index = first_col

    # Remove first column
    raw = raw.iloc[:, 1:]

    # Transpose back so samples become rows
    df = raw.T

    # Use row labels as columns
    df.columns = raw.index

    # Remove duplicate column names by appending numbers
    cols = pd.Series(df.columns)

    for dup in cols[cols.duplicated()].unique():

        dup_idx = cols[cols == dup].index

        cols.iloc[dup_idx] = [
            f"{dup}_{i}"
            if i > 0 else dup
            for i in range(len(dup_idx))
        ]

    df.columns = cols

    df.reset_index(
        drop=True,
        inplace=True
    )

    return df
