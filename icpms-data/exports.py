from io import BytesIO
import pandas as pd


def export_excel(results):

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="xlsxwriter"
    ) as writer:

        results.to_excel(
            writer,
            sheet_name="Results",
            index=False
        )

    return output.getvalue()
