# lambdata_urena
repository practicing for linux command line
Help on module lambdata_urena1.df_utils in lambdata_urena1:

NAME
    lambdata_urena1.df_utils

DESCRIPTION
    Functions and class
    Class Dead_poet_society that holds english poem information
    Function isit_float check to see if a str is formated as a float

CLASSES
    builtins.object
        Dead_poets_society

    class Dead_poets_society(builtins.object)
     |  Dead_poets_society(poem, poet, n_words, link)
     |
     |  class for english poems
     |  enter poem name, poet name,
     |  number of words in the poem,
     |  and web link to the poem
     |  type class.poem1..5 for examples
     |
     |  Methods defined here:
     |
     |  __init__(self, poem, poet, n_words, link)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    datetime_columns(df, feature)
        pass a pandas dataframe and column name with str type with datetime info,
        return columns in the same data frame with columns: day, month and year (int)

    isit_float(s)
        Function pass a string return true if it is
        formatted as a float example isit_float('1.1')
