from pathlib import Path


def get_root_directory_of_project():

    root = Path(__file__).resolve().parent.parent
    
    return root