def apply_dilution(
    df,
    isotope
):

    df[f"{isotope}_dil_corr"] = (
        df[f"{isotope}_blk_corr"]
        * df["Dilution Factor"]
    )

    return df
