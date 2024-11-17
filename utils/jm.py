import inspect

def dcl(df, DEBUG = True):
    """Print the dataframe column names in the desired format."""
    # Retrieve the name of the variable passed into the function
    frame = inspect.currentframe().f_back
    df_name = [name for name, value in frame.f_locals.items() if value is df][0]
    
    formatted_output = f"\n{df_name}[[\n\n" + ",\n\n".join(f"'{column}'" for column in df.columns) + "\n]]"
    
    if DEBUG:
        print(formatted_output)
    