from utils.loader import load_raw_data

from manipulations.cleaner import get_cleaned_chess_data



#%% test module

if __name__ == "__main__":
    
    RAW_DATA = load_raw_data()
    
    cleaned_data = get_cleaned_chess_data(RAW_DATA)
    
    
    
    





