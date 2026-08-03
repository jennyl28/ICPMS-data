import pandas as pd
import re

from scipy.stats import linregress


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
