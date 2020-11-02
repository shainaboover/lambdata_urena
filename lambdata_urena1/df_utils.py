import pandas as pd
import numpy as np
import datetime as dt

ONES = pd.Series(np.ones(10))
ZEROS = pd.Series(np.zeros(20))


def isit_float(s):
    """Function pass a string return true if it is formatted as a float example isit_float('1.1')
    returns False if it is formatted as a interger or str example isit_float('1') """
    try:
        int(s)
        return False
    except ValueError:
          try:
                float(s)
                return True
          except ValueError:
                return False


def datetime_columns(df,feature):
  """pass a pandas dataframe and column name with date str type,
  return columns in same the data frame with day, month and year columns"""
  df['day'] = pd.to_datetime(df[feature]).dt.day
  df['month'] = pd.to_datetime(df[feature]).dt.month
  df['year'] = pd.to_datetime(df[feature]).dt.month
  return df

class Dead_poets_society:
  """class for english poems"""
  def __init__(self, poem, poet, n_words,link):
    self.poem = poem
    self.poet = poet
    self.n_words = n_words
    self.link = link
  def __repr__(self):
    return f"Dead Poets Society(Poem Title={self.poem}, Name Of Poet={self.poet}, Number of Words={self.n_words},Poem's Link ={self.link})"
  def __str__(self):
    return f"Dead Poets Society(Poem Title:{self.poem}, Name Of Poet:{self.poet}, Number of Words:{self.n_words},Poem's Link :{self.link})"

poem3 = Dead_poets_society('She Walks In Beatuty', 'Lord Byron', 119,
                             "https://www.poetryfoundation.org/poems/43844/she-walks-in-beauty")
poem1 = Dead_poets_society("O Captain! My Captain!",'Walt Whitman',199,"https://www.poetryfoundation.org/poems/45474/o-captain-my-captain")
poem2 = Dead_poets_society("To the Virgins, to Make Much of Time","Robert Herrick",96,"https://www.poetryfoundation.org/poems/46546/to-the-virgins-to-make-much-of-time")
poem4 = Dead_poets_society('If—','RUDYARD KIPLING',283,'https://www.poetryfoundation.org/poems/46473/if---')
poem5 = Dead_poets_society('The Cremation of Sam McGee','ROBERT W. SERVICE',882,'https://www.poetryfoundation.org/poems/45081/the-cremation-of-sam-mcgee')