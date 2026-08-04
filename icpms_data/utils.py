import pandas as pd


def build_qc_table(df):

    qc = df[
        [
            "Sample Name",
            "Applied Blank",
            "Applied Blank Value",
            "Dilution Factor",
            "Mass Correction"
        ]
    ].copy()

    return qc
