"""
calibration_processing.py

Functions for:

- Calibration curve fitting
- CPS → Activity conversion
- Calibration QC
"""

import pandas as pd
import numpy as np

from scipy.stats import linregress


def fit_calibration_curve(
    calibration_df,
    cps_column="CPS",
    activity_column="Activity_Bq"
):
    """
    Fit linear calibration curve

    Activity = slope * CPS + intercept

    Parameters
    ----------
    calibration_df : DataFrame

    cps_column : str

    activity_column : str

    Returns
    -------
    dict
    """

    calibration_df = calibration_df.dropna(
        subset=[
            cps_column,
            activity_column
        ]
    )

    slope, intercept, r_value, p_value, std_err = (
        linregress(
            calibration_df[cps_column],
            calibration_df[activity_column]
        )
    )

    return {
        "slope": slope,
        "intercept": intercept,
        "r2": r_value ** 2,
        "p_value": p_value,
        "std_err": std_err
    }


def convert_cps_to_activity(
    cps,
    slope,
    intercept
):
    """
    Convert CPS to activity
    """

    return (
        cps * slope
        + intercept
    )


def apply_calibration_to_dataframe(
    df,
    cps_column,
    slope,
    intercept,
    output_column="Activity_Bq"
):
    """
    Apply calibration equation
    to entire dataframe
    """

    df[output_column] = (
        df[cps_column]
        * slope
        + intercept
    )

    return df


def calibration_qc_table(
    calibration_df,
    cps_column="CPS",
    activity_column="Activity_Bq"
):
    """
    Build QC table
    """

    fit = fit_calibration_curve(
        calibration_df,
        cps_column,
        activity_column
    )

    qc_df = calibration_df.copy()

    qc_df["Predicted Activity"] = (
        fit["slope"]
        * qc_df[cps_column]
        + fit["intercept"]
    )

    qc_df["Residual"] = (
        qc_df[activity_column]
        - qc_df["Predicted Activity"]
    )

    qc_df["Percent Error"] = (
        qc_df["Residual"]
        /
        qc_df[activity_column]
        * 100
    )

    return qc_df
