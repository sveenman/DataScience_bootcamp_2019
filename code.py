#This function creates a decorator which prints the shape of the output of a function
def decor_shape(func):
    def _(*args, **kwargs):
        out=func(*args, **kwargs)
        print (f'The function {func} output is a dataframe with shape: {out.shape}')
        return out
    return _

#This function rename to lowercase the columns of a pandas dataframe
@decor_shape
def lowercase_columns(df):
    return df.rename(columns = str.lower)
    


