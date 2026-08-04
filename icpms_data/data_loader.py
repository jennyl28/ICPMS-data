import pandas as pd

def load_icpms_file(uploaded_file):

    raw = pd.read_excel(
        uploaded_file,
        sheet_name=0,
        header=None
    )

    raw = raw.T

    isotope_row = raw.iloc[0]
    field_row = raw.iloc[1]

    columns = []

    for iso, field in zip(isotope_row, field_row):

        iso = "" if pd.isna(iso) else str(iso).strip()
        field = "" if pd.isna(field) else str(field).strip()

        if iso == "":
            columns.append(field)

        elif field == "":
            columns.append(iso)

        else:
            columns.append(
                f"{iso} {field}"
            )

    data = raw.iloc[2:].copy()

    data.columns = columns

    data.reset_index(
        drop=True,
        inplace=True
    )

    return data
