import pandas as pd


def load_icpms_file(uploaded_file):

    raw = pd.read_excel(
        uploaded_file,
        sheet_name=0,
        header=None
    )

    # First column contains parameter names
    headers = raw.iloc[:, 0].astype(str)

    # Locate the row where actual sample data starts
    sample_start = headers[
        headers.str.contains(
            r"\.d$",
            case=False,
            na=False
        )
    ].index[0]

    metadata = raw.iloc[:sample_start, 0]

    data = raw.iloc[sample_start:].reset_index(
        drop=True
    )

    columns = metadata.tolist()

    data = data.T

    data.columns = columns

    data = data.reset_index(
        drop=True
    )

    return data
