import pandas as pd

def load_icpms_file(uploaded_file):

    xls = pd.ExcelFile(uploaded_file)

    raw_data = pd.read_excel(
        xls,
        sheet_name=0
    )

    return raw_data
