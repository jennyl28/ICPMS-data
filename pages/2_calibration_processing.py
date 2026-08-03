import pandas as pd
import re
from pathlib import Path
from scipy.stats import linregress

def load_radionuclides():
    file_path = (
        Path(__file__).parent.parent
        / "data"
        / "radionuclides.csv")

return pd.read_csv(file_path)

def find_standards(
    df,
    sample_col="Sample Name"
):

    pattern = (
        r"(ppb|ppm|ppt|bq|kbq)"
    )

    return df[
        df[sample_col]
        .astype(str)
        .str.contains(
            pattern,
            case=False,
            regex=True
        )
    ].copy()

def extract_standard_value(
    sample_name
):

    match = re.search(
        r"(\\d+\\.?\\d*)",
        str(sample_name)
    )

    if match:

        return float(
            match.group(1)
        )

    return None

def apply_all_calibrations(
    df,
    isotope_info
):

    standards = (
        find_standards(df)
    )

    results = {}

    for isotope in isotope_info:

        col = (
            isotope["column"]
            + "_mass_corr"
        )

        if col not in df.columns:

            continue

        calibration_df = (
            standards.copy()
        )

        calibration_df[
            "Known_Conc"
        ] = calibration_df[
            "Sample Name"
        ].apply(
            extract_standard_value
        )

        calibration_df = (
            calibration_df.dropna(
                subset=["Known_Conc"]
            )
        )

        if len(calibration_df) < 2:

            continue

        slope, intercept, r, _, _ = (
            linregress(
                calibration_df[col],
                calibration_df[
                    "Known_Conc"
                ]
            )
        )

        output_col = (
            col
            + "_calculated"
        )

        df[output_col] = (
            df[col]
            * slope
            + intercept
        )

        results[col] = {
            "slope": slope,
            "intercept": intercept,
            "r2": r**2
        }

    return df, results
