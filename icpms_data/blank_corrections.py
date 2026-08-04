import pandas as pd


def apply_nearest_blank(
    df,
    isotope
):

    blank_no = 0

    current_blank = None

    blank_ids = []

    blank_values = []

    corrected = []

    for _, row in df.iterrows():

        sample = str(
            row["Sample Name"]
        ).strip().lower()

        if sample == "blank":

            blank_no += 1

            current_blank = row[isotope]

            blank_id = f"Blank_{blank_no}"

        blank_ids.append(blank_id)

        blank_values.append(current_blank)

        if current_blank is None:

            corrected.append(None)

        else:

            corrected.append(
                row[isotope]
                - current_blank
            )

    df["Applied Blank"] = blank_ids

    df["Applied Blank Value"] = blank_values

    df[f"{isotope}_blk_corr"] = corrected

    return df
