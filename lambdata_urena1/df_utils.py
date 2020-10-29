import pandas as pd
import numpy as np
import datetime as dt

ONES = pd.Series(np.ones(10))
ZEROS = pd.Series(np.zeros(20))


def isit_float(s):
    try:
        int(s)
        return False
    except ValueError:
          try:
                float(s)
                return True
          except ValueError:
                return False


def dd_mm_yyyy_columns(df,feature):
  "pass a pandas dataframe and column name with date str type, return columns in same the data frame with day, month and year columns"
  df['day'] = pd.to_datetime(df[feature]).dt.day
  df['month'] = pd.to_datetime(df[feature]).dt.month
  df['year'] = pd.to_datetime(df[feature]).dt.month
  return df
