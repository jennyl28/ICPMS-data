import pandas as pd


METADATA_COLUMNS = {
    "Rjct",
    "Data File",
    "Acq. Date-Time",
    "Type",
    "Level",
    "Sample Name"
}


def load_icpms_file(uploaded_file):

    raw = pd.read_csv(
        uploaded_file,
        header=None,
        dtype=str
    )

    isotope_row = raw.iloc[0]
    field_row = raw.iloc[1]

    columns = []
    current_isotope = None

    for iso, field in zip(isotope_row, field_row):

        iso = "" if pd.isna(iso) else str(iso).strip()
        field = "" if pd.isna(field) else str(field).strip()

        if "->" in iso or "→" in iso:
            current_isotope = iso

        # metadata fields
        if field in METADATA_COLUMNS:
            columns.append(field)

        # isotope cps
        elif field == "CPS":
            columns.append(
                f"{current_isotope}_CPS"
            )

        # isotope rsd
        elif field == "CPS RSD":
            columns.append(
                f"{current_isotope}_CPS_RSD"
            )

        else:
            columns.append(
                f"Unnamed_{len(columns)}"
            )

    df = raw.iloc[2:].copy()

    df.columns = columns

    df.reset_index(
        drop=True,
        inplace=True
    )

    return df
