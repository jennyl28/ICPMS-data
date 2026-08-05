import pandas as pd
import re


def load_icpms_file(uploaded_file):

    raw = pd.read_excel(
        uploaded_file,
        header=None
    )
    print("RAW SHAPE")
    print(raw.shape)
    print(raw.head(20))

    # First column contains row identifiers
    row_labels = raw.iloc[:, 0].astype(str)

    # Remaining columns contain samples
    values = raw.iloc[:, 1:]

    # Metadata rows
    metadata_rows = {
        "Rjct",
        "Data File",
        "Acq. Date-Time",
        "Type",
        "Level",
        "Sample Name"
    }


    # Build dataframe row-by-row
    data_rows = []

    sample_count = values.shape[1]

    for sample_idx in range(sample_count):

        row_dict = {}

        current_isotope = None

        col_data = values.iloc[:, sample_idx]

        output_col = 0

        for i, label in enumerate(row_labels):

            label = str(label).strip()

            value = col_data.iloc[i]

            if label in metadata_rows:

                row_dict[label] = value

            elif "->" in label or "→" in label:

                current_isotope = label

            elif label.strip().upper() == "CPS":

                row_dict[
                    f"{current_isotope}_CPS"
                ] = value

            elif "RSD" in label.strip().upper():

                row_dict[
                    f"{current_isotope}_CPS_RSD"
                ] = value

        data_rows.append(row_dict)

    df = pd.DataFrame(data_rows)

    print(type(df))
    print(df.shape)
    print(df.head())

    return df
