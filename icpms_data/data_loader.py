import pandas as pd


def load_icpms_file(uploaded_file):

    raw = pd.read_excel(
        uploaded_file,
        header=None
    )

    # header rows
    isotope_row = raw.iloc[0]
    field_row = raw.iloc[1]

    columns = []

    current_isotope = None

    for iso, field in zip(isotope_row, field_row):

        iso = "" if pd.isna(iso) else str(iso).strip()
        field = "" if pd.isna(field) else str(field).strip()

        # isotope label row
        if "->" in iso or "→" in iso:
            current_isotope = iso

        # metadata columns
        if field in [
            "Rjct",
            "Data File",
            "Acq. Date-Time",
            "Type",
            "Level",
            "Sample Name"
        ]:
            columns.append(field)

        # isotope measurement columns
        elif field == "CPS":
            columns.append(
                f"{current_isotope}_CPS"
            )

        elif "RSD" in field.upper():
            columns.append(
                f"{current_isotope}_CPS_RSD"
            )

        else:
            columns.append(
                f"Unnamed_{len(columns)}"
            )

    # actual data starts on row 2
    df = raw.iloc[2:].copy()

    df.columns = columns

    df.reset_index(
        drop=True,
        inplace=True
    )

    return df
