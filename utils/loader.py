import pandas as pd

from config.root_dir import get_root_directory_of_project


#%%


def load_raw_data():
    
    root_dir = get_root_directory_of_project()
    
    raw_chess_data = pd.read_csv(root_dir / "raw_data" / "games.csv")
    
    return raw_chess_data


#%% Test that the module is working


if __name__ == "__main__":
    
    
    
    
    raw_chess_data = load_raw_data()
    