import pandas as pd

def load_mass_file(uploaded_file):

    xls = pd.ExcelFile(uploaded_file)

    return {
        sheet: pd.read_excel(xls, sheet)
        for sheet in xls.sheet_names
    }
