import os

def get_current_directory():
    current_dir = os.getcwd()
    return current_dir

if __name__ == "__main__":
    print("Current directory:", get_current_directory())
