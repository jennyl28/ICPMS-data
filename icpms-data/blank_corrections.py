import pandas as pd


def assign_closest_blank(df):

    current_blank = None
    blank_lookup = []

    for _, row in df.iterrows():

        sample_name = str(row["Sample Name"]).strip()

        if sample_name.lower() == "blank":
            current_blank = row

        blank_lookup.append(current_blank)

    df["Assigned Blank"] = blank_lookup

    return df
