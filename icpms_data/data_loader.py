import pandas as pd


def load_icpms_file(uploaded_file):

    # Read workbook
    raw = pd.read_excel(
        uploaded_file,
        sheet_name=0,
        header=None
    )

    # Transpose
    raw = raw.T

    # Generate headers from first two rows
    headers = []

    for i in range(len(raw.columns)):

        isotope = raw.iloc[0, i]
        field = raw.iloc[1, i]

        isotope = (
            ""
            if pd.isna(isotope)
            else str(isotope).strip()
        )

        field = (
            ""
            if pd.isna(field)
            else str(field).strip()
        )

        # Ignore qualification messages
        if (
            "Calibration Curve Fit"
            in isotope
            or "CPS RSD value"
            in isotope
        ):
            headers.append(
                f"Warning_{i}"
            )

        elif isotope == "Sample":

            headers.append(
                "Sample"
            )

        elif isotope == "":

            headers.append(
                field
            )

        elif field == "":

            headers.append(
                isotope
            )

        else:

            headers.append(
                f"{isotope}_{field}"
            )

    # Remove first two rows
    df = raw.iloc[2:].copy()

    # Apply headers
    df.columns = headers

    # Remove warning columns
    df = df.loc[
        :,
        ~df.columns.str.startswith(
            "Warning_"
        )
    ]

    # Reset index
    df.reset_index(
        drop=True,
        inplace=True
    )

    return df
