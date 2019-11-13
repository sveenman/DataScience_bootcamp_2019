def decor_shape(func):
    def _(*args, **kwargs):
        out=func(*args, **kwargs)
        print (f'The function {func} output is a dataframe with shape: {out.shape}')
        return out
    return _


