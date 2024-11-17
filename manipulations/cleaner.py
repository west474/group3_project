import pandas as pd

from utils.loader import load_raw_data

"""

Stages of cleaning:
    
    
    I want to keep my stages of cleaning in line in the variable explorer of Spyder
    
    so I am going to prefix each stange with a capital letter A, B, C, etc. 
    
    capital letters are good because you can select to exclude them from the drop down menu in variable explorer.
    
    
    
    I'm making sanity checks all caps so that I can also exclude these.



stage A: load data


Review of variables:


    let's keep the id variable so that we know we are dealing with distinct games.
    
    First lets check if our games are unique:
        
        
        sources:
            
        https://stackoverflow.com/questions/50242968/check-for-duplicate-values-in-pandas-dataframe-column
        
        https://stackoverflow.com/questions/35584085/how-to-count-duplicate-rows-in-pandas-dataframe
    
        
    
    Stage B: Remove duplicate ids:
        
    The games are not unique so let's select only the first game from duplicated games. 
    
    
    
    
    
    
    
    
    ------------------------------------------------------------------------------------
    
    The thinking behind this is that any given player may have lurking/hidden attributes that could account for elevated performance. 
    
    
    
    If we have many games by a player who has say a great coach, and just happens to play an obscure oppening,
    
    we may falsely believe that the oppening is contributing to the success of this player while in fact it is his general coaching. 
    
    
    Our focus should not be on whether or not an individual player or group of players perform well
    
    at the lower levels of chess but rather does the opening itself perform well. 
    
    I believe that by having only one game per player we help to insulate our prime variable:
        
        opening, from unwanted influences of the player variable.


"""


def check_that_our_ids_are_unique(chess_data, DEBUG = True):
    
    duplicated_ids = chess_data['id'].duplicated().any()
    
    num_players = len(chess_data['id'])

    num_players_without_duplication = len(chess_data['id'].drop_duplicates())

    num_duplicate_ids = num_players - num_players_without_duplication
    
    if DEBUG:
        
        if duplicated_ids == True:
            
            print(f"\nthere are {num_duplicate_ids} duplicated id's in our data set.")
            
        else:
            
            print("\nthere are NO duplicated id's in our data set.")
        
        
def select_first_game_in_data_from_each_id(chess_data):
    
    """ 
    
    "first" is default argument for drop duplicates so doesn't need to be specified.
    
    https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.drop_duplicates.html
    
    """ 
    
    unique_id_chess_data = chess_data.drop_duplicates(subset='id')
    
    
    return unique_id_chess_data


def get_rated_games(chess_data):
    
    rated_games = chess_data[chess_data["rated"]==True]
    
    return rated_games
    
    
    

def convert_unix_time_to_timestamps(chess_data, columns: tuple):
    
    
    for column in columns:
        
        
        chess_data.loc[:, column] = pd.to_datetime(chess_data[column], unit= "ms")
        
    return chess_data




def remove_draws(chess_data, does_remove_all_draws = True):
    
    if does_remove_all_draws == False:
        # this still leaves some draws. See below for explanation
        
        no_draws = chess_data[chess_data["victory_status"]!="draw"] 
        
        row1 = test_duplicates.loc[18642]
        row2 = test_duplicates.loc[3882]

        are_rows_equal = row1.equals(row2)
        
        print("Are rows 18642 and 3882 identical?", are_rows_equal)
    
    
    # This removes remaining draws from the data
    no_draws = chess_data[chess_data["winner"]!="draw"]
    
    
    return no_draws

    
    
    



#%% Test cleaner

if __name__ == "__main__":
    
    
    #%% A -- load data
    
    A_raw_chess_data = load_raw_data()
    
    
    
    #%% B -- Remove duplicate ids

    check_that_our_ids_are_unique(A_raw_chess_data, DEBUG = True)
    
    
    
    
    
    
    
    B_unique_id_chess_data = select_first_game_in_data_from_each_id(A_raw_chess_data)
    
    check_that_our_ids_are_unique(B_unique_id_chess_data, DEBUG = True)
    
    #%% C -- Remove all non rated games.
    
    
    C_rated_games = get_rated_games(B_unique_id_chess_data)
    
    
    #%% D -- convert unix epoch time columns to time stamps
    
    """
    
    https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html
    
    https://stackoverflow.com/questions/55449747/convert-column-of-epoch-timestamps-to-datetime-with-timezone
    
    """
    
    D_good_times = convert_unix_time_to_timestamps(C_rated_games, ("created_at", "last_move_at"))
    
    
    #%% E -- Remove all draws
    
    E_no_draws = remove_draws(D_good_times)
    
    
    #%% sanity check that draws have been removed
    
    Z_SC_A_OUTCOMES = E_no_draws.winner.unique()
    
    # Draws still seem to be present
    
    #
    
    Z_SC_A_DRAWS = E_no_draws[E_no_draws["winner"] == "draw"]
    
    """
    
    Victory status => out_of_time can lead to a draw too (in rare cases).
    
    This will only happen if a player who is winning runs out of time and
    
    his opponent doesn't have enough material to deliver a checkmate
    
    
    In my first attempt to remove draws I did not sucessfully remove this type of draw. 
    
    so 37/15467 remained. 
    
    
    This is perhaps insignificant at ~ 0.24% of our data
    
    but I will refactor our remove draw function to correct this anyway
    
    
    """
    
    #%% Inspect time data
    
    Z_I_A_TIME = E_no_draws.increment_code.unique() 
    
    """
    
    There are 344 unique time increment codes.
    
    
    this is more than I thought there would be.
    
    
    
    
    For the moment I think we don't need to filter out any time increment. 
    
    
    But it may be beneficial in the future to filter our data to look at game types:
        
        
        Bullet < 3 mins
        
        3 mins <= Blitz < 10mins
        
        10 mins <= Rapid < 60 mins
        
        60 mins <= Classical 
        
        
    
    """
    

    
 #%%   
    





