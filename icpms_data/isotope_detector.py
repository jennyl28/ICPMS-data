import re


def detect_isotope_columns(df):
    """
    Detect all ICP-MS isotope columns.
    """

    isotopes = []

    pattern = (
        r"(\\d+)\\s*->\\s*(\\d+)\\s+"
        r"([A-Za-z]+)"
        r".*?\\[\\s*(.*?)\\s*\\]"
    )

    for col in df.columns:

        match = re.search(pattern, str(col))

        if match:

            isotopes.append({
                "column": col,
                "mass": int(match.group(1)),
                "element": match.group(3),
                "gas": match.group(4)
            })

    return isotopes
