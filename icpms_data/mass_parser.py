import pandas as pd


def load_mass_file(uploaded_file):

    xls = pd.ExcelFile(uploaded_file)

    sheets = {}

    for sheet in xls.sheet_names:
        sheets[sheet] = pd.read_excel(
            xls,
            sheet_name=sheet
        )

    return sheets
