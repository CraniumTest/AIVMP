import pandas as pd

def load_data(volunteer_path, nonprofit_path):
    volunteers_df = pd.read_csv(volunteer_path)
    nonprofits_df = pd.read_csv(nonprofit_path)

    return volunteers_df, nonprofits_df
