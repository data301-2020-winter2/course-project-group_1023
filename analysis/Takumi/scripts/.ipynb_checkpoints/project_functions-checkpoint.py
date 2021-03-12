import pandas as pd
import numpy as np
def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .drop(columns=['Evaporation','Sunshine','Cloud9am','Cloud3pm','RainToday','RainTomorrow'])
          .rename(columns={'Rainfall':"Percipitation"})
          .dropna()
          
      )

    # Method Chain 2 (Resetting index)

    df2 = (
          df1
          .reset_index(drop=True)
      )

    # Make sure to return the latest dataframe

    return df2 