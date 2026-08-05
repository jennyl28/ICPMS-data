import re


def detect_isotope_columns(df):

    isotopes = []

    pattern = re.compile(
        r"(\d+)\s*(?:->|→)\s*(\d+)\s+([A-Za-z]+)"
    )

    for col in df.columns:

        col = str(col)

        if not col.endswith("_CPS"):
            continue

        match = pattern.search(col)

        if match:

            isotopes.append(
                {
                    "column": col,
                    "mass": int(match.group(2)),
                    "element": match.group(3)
                }
            )

    return isotopes
