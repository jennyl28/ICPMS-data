def apply_mass_correction(
    df,
    isotope
):

    df[f"{isotope}_mass_corr"] = (
        df[f"{isotope}_dil_corr"]
        * df["Mass Correction"]
    )

    return df
