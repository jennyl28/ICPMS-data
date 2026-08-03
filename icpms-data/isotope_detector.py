import re


def detect_isotope_columns(df):
    """
    Detect all ICP-MS isotope columns.

    Returns
    -------
    list of dict

    Example:

    [
        {
            "column": "88 -> 88  Sr  [ No Gas ]",
            "element": "Sr",
            "mass": 88,
            "gas": "No Gas"
        }
    ]
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
